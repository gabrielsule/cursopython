try:
    numero = int(input("ingrese un número: "))
    factor = numero / 0
except (ValueError, ZeroDivisionError):
    print("ha ingresado un valor cero o no numérico")
else:
    print(f"el valor es: {numero}")