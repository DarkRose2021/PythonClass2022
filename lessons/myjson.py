#json
{
    "emp": [
            {"name": 
                "scott", 
                "age":25},
            {"name": 
                "david", 
                "age":30}
    ]
}

data = '{"name":"scott", "age":21, "type":"zombie"}'

import json
datajson = json.loads(data)
print(datajson)

print(datajson['name'])

stringdata = json.dumps(datajson)
print(stringdata)

with open('test.json', 'w') as file1:
    file1.write(stringdata)

db = [
    {'brand': 'toyota', 'model':'corrola'},
    {'brand': 'honda', 'model':'civic'},
]

with open('test2.json', 'w') as file2:
    json.dump(db, file2, indent=4)

with open('test2.json', 'r') as file3:
    vehicles = json.load(file3)

for v in vehicles:
    print(v['brand', v['model']])