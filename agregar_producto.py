def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingrese un valor numérico válido.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Ingrese un número entero válido.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto agregado correctamente.\n")