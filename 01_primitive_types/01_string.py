# una línea
course = "curso de python"

print(len(course))
print(course[0])
print(course[-1])
print(course[0:5])

# multi línea
courses = """
python
node
javascript
"""

print(courses)

# Caracteres de escape
# \"
# \'
# \\
# \n

# Formateo
first = "Gabriel"
last = "Sulé"
full = f"{last}, {first}"
print(full)

# Métodos
print(course.upper)
print(course.lower)
print(course.title)
print(course.lstrip)
print(course.rstrip)
print(course.find("py"))
print(course.replace("py", "pi"))
print("y" in course)

