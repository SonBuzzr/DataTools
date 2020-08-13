import json

with open('package_info.json', 'r') as f:
    data = json.load(f)

print(data)