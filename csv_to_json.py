import csv, json
csvFilePath = "my_file.csv"
jsonFilePath = "my_file.json"

# read the csv and store in dictionary
data = {}
with open(csvFilePath, encoding='utf-8-sig') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        my_column = csvRow["my_column"]
        data[my_column] = csvRow

# # [Option] add a json root node
# root = {}
# root["my_root_node"] = data

# write to json
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))   # If [Option] above is enabled, "data" should be updated to "root"

