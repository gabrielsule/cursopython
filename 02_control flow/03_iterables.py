for i in range(5):
    print("lorem", i + 1)

for i in range(5):
    print("lorem", i + 1, (i + 1) * "*")

for i in range(1, 10, 2):
    print("lorem", i + 1, (i + 1) * "*")    

for i in range(5):
    for j in range(3):
        print(f"{i}, {j}")

for i in "lorem":
    print(i) 

for i in [1,2,3,4,5]:
    print(i)    


num = 100
while num > 0:
    print(num)
    num //= 2

command = ""
while command != "exit":
    command = input("escriba exit para salir ")
    print(command)    