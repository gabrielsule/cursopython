def multiplicar1(x, y):
    print(x * y)

multiplicar1(2, 3)


def multiplicar2(*numeros):
    for i in numeros:
        print(i)

multiplicar2(2, 3, 4)


def multiplicar3(*numeros):
    total = 1
    
    for i in numeros:
        total *= i

    return total

print(multiplicar3(2, 3, 4))


def ver(**data):
    print(data)
    print(data["id"])
    print(data["nombre"])

ver(id=2, nombre="gabriel")


