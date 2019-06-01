try:
    numero = int(input("ingrese un número: "))
except ValueError:
    print("no ha ingresado un valor numérico")
else:
    print(f"el valor es: {numero}")