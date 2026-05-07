import json

# load files
with open("results.json", "r") as f:
    results = json.load(f)

with open("details.json", "r") as f:
    details = json.load(f)

database = {}

for key in results:
    database[key] = {}

    # first add results.json values
    database[key].update(results[key])

    # then add details.json values
    if key in details:
        database[key].update(details[key])

# write new json
with open("database.json", "w") as f:
    json.dump(database, f, indent=4)

print("database.json created successfully")
