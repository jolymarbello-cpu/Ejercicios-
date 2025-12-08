def buscar_nombre(nombres, nombre_buscar):
    for nombre in nombres:
        if nombre.lower() == nombre_buscar.lower():
            return True
    return False

# Ejemplo de uso
lista_nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
nombre = input("Ingrese un nombre para buscar: ")
encontrado = buscar_nombre(lista_nombres, nombre)
print(f"El nombre '{nombre}' {'SÍ' if encontrado else 'NO'} está en la lista.")