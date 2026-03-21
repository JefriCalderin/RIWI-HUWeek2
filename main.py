import os
import time

from agregar_producto import agregar_producto
from mostrar_inventario import mostrar_inventario
from calcular_estadisticas import calcular_estadisticas

inventario = []

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 40)
    print("     ==== MENU INVENTARIO ====   ")
    print("=" * 40)
    print("  [1] - Agregar producto")
    print("  [2] - Mostrar inventario")
    print("  [3] - Calcular estadísticas")
    print("  [4] - Salir")
    print("=" * 40)

    opcion = input("\nElija una opción del menú: ")

    if opcion == "1":
        agregar_producto(inventario)
        input("Presione Enter para continuar...")

    elif opcion == "2":
        mostrar_inventario(inventario)
        input("Presione Enter para continuar...")

    elif opcion == "3":
        calcular_estadisticas(inventario)
        input("Presione Enter para continuar...")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")
        input("Presione Enter para continuar...")