import csv

rows = []
with open("PKN.WA.csv", "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for line in csv_reader:
        rows.append(line)

print(header)
print(rows)