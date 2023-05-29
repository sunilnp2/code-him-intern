from bs4 import BeautifulSoup
import lxml
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
response = requests.get(url)
# print(response)

response = response.text
soup = BeautifulSoup(response, "lxml")
# print(soup)

soup_table =  soup.table
# print(soud_table)

tags = soup_table.find_all('tr')
# print(tags)

data = []
for i in tags:
  data.append(i.text)

# print(data)

datas = data[0:25]
heading = data[0]

final_output = []
for i in datas:
  i = i.replace('\n','*')
  x = i.split('*')[0:11]
  final_output.append(x)

# print(final_output)

import csv
with open('worldo.csv', 'w',newline ='') as csv_writer:
    x = csv.writer(csv_writer)
    for i in final_output:
        x.writerow(i)


# import pandas as pd
# df = pd.read_csv('worldo.csv')

# print(df.iloc[8:])


