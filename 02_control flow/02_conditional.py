sueldo = 23

if sueldo < 50:
    print("sueldo bajo")
elif sueldo == 50:
    print("sueldo promedio")
else:
    print("sueldo alto")


if sueldo <= 50:
    msg = "sueldo bajo"
else:
    msg = "sueldo alto" 
print(msg)


msg = "sueldo bajo" if sueldo <= 50 else "sueldo alto"
print(msg)