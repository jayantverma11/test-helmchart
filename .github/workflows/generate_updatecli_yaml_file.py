import yaml

# Define the YAML content
yaml_content = {
    "sources": {
        "helm": {
            "name": "Get Latest Helm Chart Version",
            "kind": "helmChart",
            "spec": {
                "url": "https://kubernetes.github.io/ingress-nginx",
                "name": "ingress-nginx",
                "version": "latest"
            }
        }
    },
    "targets": {
        "updateChartVersion": {
            "name": "Update Helm Chart Version in Codebase",
            "kind": "terraform/file",
            "spec": {
                "file": "templates/eks/inputs.tf",
                "path": "variable.NGINX_CHART_VERSION.default"
            }
        }
    }
}

# Write the YAML content to a file
with open("updatecli.yaml", "w") as yaml_file:
    yaml.dump(yaml_content, yaml_file, default_flow_style=False)

print("updatecli.yaml file created successfully.")
