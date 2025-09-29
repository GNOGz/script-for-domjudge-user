import json
import csv

def checkBool(a:str):
    if(a.lower() == "true"):
        return True
    elif(a.lower() == "false"):
        return False
    else:
        raise ValueError("Input must be only true or false")

group = []
with open("./sheet_data/groups.tsv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file,delimiter='\t')
    next(reader) #skip header line
    for line in reader:
        # print(line) <- uncomment this to see the data format.
        # print(line[2])
        print(len(line))
        value = {"id":line[0],"name":line[1]}
        if(len(line) > 2): #check if boolean hidden exist in tsv
            value = {"id":line[0],"name":line[1],"hidden":checkBool(line[2])}
        group.append(value)
with open("./domjudge_data/groups.json", "w",encoding="utf-8") as f:
    json.dump(group, f, indent=4,ensure_ascii=False) 
    #indent = 4 to make it easier to read
    #ensure_ascii make it works for Thai language
print("Data saved to JSON, Please check groups.json")