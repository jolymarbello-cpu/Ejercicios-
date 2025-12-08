USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

intentos = 3
while intentos > 0:
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contraseña: ")
    
    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        print("¡Acceso concedido!")
        break
    else:
        print(f"Credenciales incorrectas. Intentos restantes: {intentos - 1}")
        intentos -= 1
else:
    print("Acceso denegado. Demasiados intentos fallidos.ñ")