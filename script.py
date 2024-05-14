import subprocess

def install_helm():
    subprocess.run(["curl", "-fsSL", "-o", "get_helm.sh", "https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3"])
    subprocess.run(["chmod", "700", "get_helm.sh"])
    subprocess.run(["./get_helm.sh"])

def install_prometheus():
    subprocess.run(["helm", "repo", "add", "prometheus-community", "https://prometheus-community.github.io/helm-charts"])
    subprocess.run(["helm", "repo", "update"])
    subprocess.run(["helm", "install", "monitoring-stack", "prometheus-community/kube-prometheus-stack", "-n", "monitoring"])

def add_loki_repo():
    subprocess.run(["helm", "repo", "add", "loki", "https://grafana.github.io/loki/charts"])
    subprocess.run(["helm", "repo", "update"])

def install_loki():
    add_loki_repo()
    subprocess.run(["helm", "upgrade", "--install", "loki", "loki/loki-stack", "-n", "monitoring"])

def main():
    install_helm()
    install_prometheus()
    install_loki()

if __name__ == "__main__":
    main()