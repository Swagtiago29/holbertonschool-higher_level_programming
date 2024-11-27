#!/usr/bin/python3
import csv

content=[
    ['name', 'Age', 'City'],
    ['Alice', 12, 'Montreal'],
    ['Lucy', 29, 'Australia'],
    ['Mario', 69, 'Mushroom Kingdom']
]
with open("txt_folder/data.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(content)

with open("txt_folder/data.csv", 'r') as f1:
    reader = csv.reader(f1)
    rows = list(reader)
for i in rows:
    for rows in i:
        print(rows, end=' ')
    print()