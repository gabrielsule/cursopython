items = [
    ("data1", 22),
    ("data2", 11),
    ("data3", 33),
]

items.sort(key=lambda item: item[1])
print(items)

x = map(lambda item:item[1], items)
for i in x:
    print(i)

x = list(filter(lambda item:item[1] >= 20, items))
print(x)    