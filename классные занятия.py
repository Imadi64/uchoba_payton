import csv

with open('vps.csv', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    procent = int(input())
    for index, row in enumerate(reader):
        if index > 0:
            if int(row[4]) >= procent:
                print(row[0])
