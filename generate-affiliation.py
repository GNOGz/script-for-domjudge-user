import json
import csv

team_affiliation = []
with open("./sheet_data/affiliation.tsv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file,delimiter='\t')
    next(reader) #skip header line
    for line in reader:
        # print(line) <- uncomment this to see the data format.
        value = {"id":line[0],"name":line[1],"formal_name":line[2],"country":line[3]}
        team_affiliation.append(value)
with open("./domjudge_data/organizations.json", "w",encoding="utf-8") as f:
    json.dump(team_affiliation, f, indent=4,ensure_ascii=False) 
    #indent = 4 to make it easier to read
    #ensure_ascii make it works for Thai language
print("Data saved to JSON, Please check organizations.json")