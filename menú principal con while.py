def saludar():
    print("¡Hola! Bienvenido al programa.")

def calcular():
    num1 = float(input("Ingrese primer número: "))
    num2 = float(input("Ingrese segundo número: "))
    print(f"Suma: {num1 + num2}")

while True:
    print("=== MENÚ ===")
    print("1. Saludar")
    print("2. Calcular")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        saludar()
    elif opcion == "2":
        calcular()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")