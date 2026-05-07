import os
import json

# Folder containing all json files
JSON_FOLDER = "JSON Files"

merged_data = {}

for file in os.listdir(JSON_FOLDER):

    # skip the final output file
    if file.endswith(".json") and file != "details.json":

        path = os.path.join(JSON_FOLDER, file)

        with open(path, "r") as f:
            data = json.load(f)

        # merge dictionaries
        merged_data.update(data)

# write final merged json
output_path = os.path.join(JSON_FOLDER, "details.json")

with open(output_path, "w") as f:
    json.dump(merged_data, f, indent=4)

print("All JSON files merged into details.json")
