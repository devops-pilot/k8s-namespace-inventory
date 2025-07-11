from kubernetes import client, config
from tabulate import tabulate
from colorama import Fore, Style

# Load kube config from default context
config.load_kube_config()

v1 = client.CoreV1Api()

print(f"\n🔍 Fetching Namespace Inventory...\n")

table = []

namespaces = v1.list_namespace().items
for ns in namespaces:
    name = ns.metadata.name
    pods = v1.list_namespaced_pod(namespace=name).items
    services = v1.list_namespaced_service(namespace=name).items
    configmaps = v1.list_namespaced_config_map(namespace=name).items
    secrets = v1.list_namespaced_secret(namespace=name).items

    total = len(pods) + len(services) + len(configmaps) + len(secrets)
    color = Fore.RED if total == 0 else Fore.GREEN

    table.append([
        name,
        len(pods),
        len(services),
        len(configmaps),
        len(secrets),
        f"{color}{'Empty' if total == 0 else '✔️ Active'}{Style.RESET_ALL}"
    ])

print(tabulate(
    table,
    headers=["Namespace", "Pods", "Services", "ConfigMaps", "Secrets", "Status"],
    tablefmt="pretty"
))
