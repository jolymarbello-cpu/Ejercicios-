lista_compras = []

print("Escribe artículos en tu lista de compras para anadir al carrito")
print("   (escribe 'fin' para finalizar)")
print("-" * 35)


while True:
    articulo = input("articulo: ").strip()
    if articulo.lower() == 'fin':
        break
    lista_compras.append(articulo.capitalize())


print("SI TU LISTA DE COMPRAS:")
print("=" * 25)
for i, articulo in enumerate(lista_compras, 1):
    print(f"{i}. {articulo}")

print(f"Sup Total: {len(lista_compras)} articulos")
        