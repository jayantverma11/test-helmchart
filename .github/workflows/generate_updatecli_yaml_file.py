import json
import yaml
import os

# Path to the charts.json file
charts_json_path = '.github/workflows/charts.json'

# Check if the file exists and is not empty
if not os.path.exists(charts_json_path):
    raise FileNotFoundError(f"The file {charts_json_path} does not exist.")
if os.path.getsize(charts_json_path) == 0:
    raise ValueError(f"The file {charts_json_path} is empty.")

# Load chart data from JSON file
with open(charts_json_path, 'r') as json_file:
    try:
        charts = json.load(json_file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON file: {e}")

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
updatecli_yaml_path = ".github/workflows/updatecli.yaml"
with open(updatecli_yaml_path, "w") as yaml_file:
    yaml.dump(yaml_content, yaml_file, default_flow_style=False)

print(f"updatecli.yaml file created successfully at {updatecli_yaml_path}.")
