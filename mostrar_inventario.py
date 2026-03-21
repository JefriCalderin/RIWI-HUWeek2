def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
        print("\nInventario actual:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()