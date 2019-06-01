data = [1, 2, 3, 4, 5, 6]
uno, dos, *otros = data
print(otros)

for i in data:
    print(i)

for i in enumerate(data):
    print(i)
    print(i[0])    