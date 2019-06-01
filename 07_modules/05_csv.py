import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "data"])
    writer.writerow(["1", "lorem"])
    writer.writerow(["2", "ipsum"])

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
