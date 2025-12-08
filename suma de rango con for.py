inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))
suma = 0
for i in range(inicio, fin + 1):
    suma += i
print(f"La suma total es: {suma}")