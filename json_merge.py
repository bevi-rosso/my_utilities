import json

file1 = "file1.json"
file2 = "file2.json"

# read in json files
with open(file1) as jsonFile1:
    data1 = json.load(jsonFile1)

with open(file2) as jsonFile2:
    data2 = json.load(jsonFile2)

merged = dict(list(data1.items()) + list(data2.items()))

# write the merged jsons as combined file
jsonFilePath = "combined.json"

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(merged, indent=4))