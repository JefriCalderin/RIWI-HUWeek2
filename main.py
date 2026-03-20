import os
import time

# Lista donde se almacenarán todos los productos del inventario
inventario = []

# Función para agregar productos al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")

    # Validación del precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingrese un valor numérico válido.")

    # Validación de la cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Ingrese un número entero válido.")

    # Crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Guardar producto en la lista inventario
    inventario.append(producto)

    print("Producto agregado correctamente.\n")


# Función para mostrar todos los productos
def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
        print("\nInventario actual:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()


# Función para calcular estadísticas
def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos en el inventario.\n")
    else:
        valor_total = 0
        total_productos = 0

        for producto in inventario:
            valor_total += producto["precio"] * producto["cantidad"]
            total_productos += producto["cantidad"]

        print("\nEstadísticas del inventario:")
        print(f"Valor total del inventario: {valor_total}")
        print(f"Cantidad total de productos: {total_productos}\n")


# Menú principal con bucle while
while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 40)
    time.sleep(0.3)
    print("     ==== MENU INVENTARIO ====   ")
    time.sleep(0.3)
    print("=" * 40)
    time.sleep(0.3)
    print("  [1] - Agregar producto")
    time.sleep(0.3)
    print("  [2] - Mostrar inventario")
    time.sleep(0.3)
    print("  [3] - Calcular estadísticas")
    time.sleep(0.3)
    print("  [4] - Salir")
    time.sleep(0.3)
    print("=" * 40)
    time.sleep(0.5)

    opcion = input("\nElija una opción del menú: ")

    if opcion == "1":
        os.system("cls" if os.name == "nt" else "clear")
        agregar_producto()
        input("Presione Enter para continuar...")

    elif opcion == "2":
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_inventario()
        input("Presione Enter para continuar...")

    elif opcion == "3":
        os.system("cls" if os.name == "nt" else "clear")
        calcular_estadisticas()
        input("Presione Enter para continuar...")

    elif opcion == "4":
        os.system("cls" if os.name == "nt" else "clear")
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")