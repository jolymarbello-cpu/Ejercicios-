numero_tabla = int(input("Ingrese un número para la tabla: "))
operacion = input("Seleccione operación (Suma, Resta, Multi, Div): ").upper()

print(f"Tabla del {numero_tabla} ({operacion}):")
for i in range(1, 11):
    if operacion == "SUMA":
        resultado = numero_tabla + i
        print(f"{numero_tabla} + {i} = {resultado}")
    elif operacion == "RESTA":
        resultado = numero_tabla - i
        print(f"{numero_tabla} - {i} = {resultado}")
    elif operacion == "MULTI":
        resultado = numero_tabla * i
        print(f"{numero_tabla} x {i} = {resultado}")
    elif operacion == "DIV":
        if i != 0:
            resultado = numero_tabla / i
            print(f"{numero_tabla} ÷ {i} = {resultado:.2f}")
print()