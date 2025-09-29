import json
import csv
import yaml   # 👈 need to install first: pip install pyyaml

users = []
with open("./sheet_data/users.tsv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter="\t")
    next(reader)  # skip header line
    for line in reader:
        value = {
            "id": line[0],
            "username": line[1],
            "password": line[2],
            "type": line[3],
            "team_id": line[4],
            "name":line[5]
        }
        users.append(value)

# # Save JSON
# with open("./domjudge_data/teams.json", "w", encoding="utf-8") as f:
#     json.dump(team_affiliation, f, indent=4, ensure_ascii=False)

# Save YAML
with open("./domjudge_data/accounts.yaml", "w", encoding="utf-8") as f:
    yaml.dump(users, f, allow_unicode=True, sort_keys=False)  
    # allow_unicode=True keeps Thai readable
    # sort_keys=False prevents reordering of keys

print("Data saved to YAML, please check accounts.yaml")
