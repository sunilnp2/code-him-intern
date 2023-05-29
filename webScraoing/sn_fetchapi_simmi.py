import requests
import json
import csv
data = requests.get('https://api.simmifoundation.tech/api/story-of-change/')
# print(data.text)

dict = json.loads(data.text)

length = len(dict)
# for i in range(0,length):
#     print(dict[i])


with open('simmi.csv', 'a', newline='') as f:
    for i in range(0,length):
        writer = csv.writer(f)
        writer.writerow(dict[i].values())
