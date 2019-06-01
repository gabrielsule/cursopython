letras = ["a", "b", "c", "d", "e"]
varios = [6] * 3
numeros = list(range(20))
caracteres = list("lorem impsum")

print(len(letras))
print(letras[2])
letras[2] = "f"
print(letras[:3])

print(numeros)
print(numeros[::2])
print(numeros[::-1])

data = [1, 2, 3, 4, 5, 6]
uno, dos, *otros = data
print(otros)