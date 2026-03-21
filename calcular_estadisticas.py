def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        print("No hay productos en el inventario.\n")
    else:
        valor_total = 0
        total_productos = 0

        for producto in inventario:
            valor_total += producto["precio"] * producto["cantidad"]
            total_productos += producto["cantidad"]

        print("\nEstadísticas del inventario:")
        print(f"\nValor total del inventario: {valor_total}")
        print(f"Cantidad total de productos: {total_productos}\n")