import random
import string

print(random.random())
print(random.randint(1, 50))
print(random.choice([1, 2, 3, 4, 5]))
print("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)))

print(string.ascii_letters)
print(string.digits)

print("".join(random.choices(string.ascii_letters + string.digits, k=8)))
