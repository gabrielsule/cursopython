def saludo1(nombre):
    print(f"Hola {nombre}")

saludo1("Gabriel")


def saludo2(nombre):
    return f"Hola {nombre}"

print(saludo2("Gabriel"))


def saludo3(nombre="Lorem"):
    return f"Hola {nombre}"

print(saludo3())