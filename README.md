# 📦 Kubernetes Namespace Inventory CLI

Simple CLI tool to inspect all namespaces in your Kubernetes cluster and count key resources.

---

## 🔍 Features

- Lists all Kubernetes namespaces
- Shows:
  - Number of Pods
  - Number of Services
  - Number of ConfigMaps
  - Number of Secrets
- Flags empty or unused namespaces
- Color-coded status

---

## 📁 Structure
```
k8s-namespace-inventory/
├── inventory.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
## 2. Make sure your kubectl context is set
```
kubectl config current-context
```
## 3. Run the script
```
python3 inventory.py
```
## 🧪 Sample Output
```
🔍 Fetching Namespace Inventory...

+-------------+------+----------+------------+---------+--------+
| Namespace   | Pods | Services | ConfigMaps | Secrets | Status |
+-------------+------+----------+------------+---------+--------+
| default     | 3    | 1        | 2          | 5       | ✔️ Active |
| kube-system | 10   | 3        | 8          | 10      | ✔️ Active |
| test-ns     | 0    | 0        | 0          | 0       | Empty   |
+-------------+------+----------+------------+---------+--------+
```
## 📌 Notes
- Requires access to the cluster via kubectl
- Works with both minikube and cloud clusters
- No cluster changes are made
## 📝 License
- MIT
## 🙌 Contribute
- Feel free to fork & improve — PRs welcome!
