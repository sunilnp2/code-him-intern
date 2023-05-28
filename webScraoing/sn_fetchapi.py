import requests
import json
import csv
data = requests.get('https://jsonplaceholder.typicode.com/todos/1')

datas = data.text
python_dict = json.loads(datas)
print(python_dict)

# for d in datas:
#     print(d)
with open('json.csv', 'a') as csv_writer:
    write = csv.writer(csv_writer)
    write.writerow(python_dict.values())