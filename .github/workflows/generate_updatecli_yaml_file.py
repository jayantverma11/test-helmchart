import json
import yaml

# Path to the charts.json file
charts_json_path = '.github/workflows/chart.json'

# Load chart data from JSON file
with open(charts_json_path, 'r') as json_file:
    charts = json.load(json_file)

yaml_content = {
    "sources": {},
    "targets": {}
}

for chart in charts:
    source_name = f"get_{chart['chart']}_version"
    target_name = f"update_{chart['chart']}_version"

    yaml_content["sources"][source_name] = {
        "name": f"Get Latest {chart['chart']} Helm Chart Version",
        "kind": "helmChart",
        "spec": {
            "url": chart["repository"],
            "name": chart["chart"],
            "version": "latest"
        }
    }

    yaml_content["targets"][target_name] = {
        "name": f"Update {chart['chart']} Helm Chart Version in Codebase",
        "kind": "terraform/file",
        "spec": {
            "file": "templates/eks/inputs.tf",
            "path": f"variable.{chart['tf_version_var_name']}.default"
        }
    }

# Write the YAML content to a file
with open(".github/workflows/updatecli.yaml", "w") as yaml_file:
    yaml.dump(yaml_content, yaml_file, default_flow_style=False)

print("updatecli.yaml file created successfully.")
