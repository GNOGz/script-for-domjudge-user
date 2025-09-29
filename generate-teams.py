import json
import csv

teams = []
with open("./sheet_data/teams.tsv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file,delimiter='\t')
    next(reader) #skip header line
    for line in reader:
        # print(line) <- uncomment this to see the data format.
        value = {"id":line[0],"group_ids":[line[2]],"name":line[3],"organization_id":line[4],"location.description":line[5]}
        teams.append(value)
with open("./domjudge_data/teams.json", "w",encoding="utf-8") as f:
    json.dump(teams, f, indent=4,ensure_ascii=False) 
    #indent = 4 to make it easier to read
    #ensure_ascii make it works for Thai language
print("Data saved to JSON, Please check teams.json")