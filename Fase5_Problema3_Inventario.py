"""
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Fundamentos de Programación (213022)
Fase 5 - Evaluación Final POA
Estudiante: Henry Santiago Buitrago Rojas

Problema 3: Inventario y reabastecimiento
A partir de una matriz con el inventario de una bodega, el programa
determina la cantidad exacta que se debe pedir de cada artículo.
"""

inventario = [
    ["A001", "Tornillos 1/4 pulgada", 120, 100],
    ["A002", "Tuercas hexagonales", 35, 80],
    ["A003", "Arandelas planas", 80, 80],
    ["A004", "Cable eléctrico 12 AWG", 10, 50],
    ["A005", "Cinta aislante", 60, 40],
    ["A006", "Brocas de 6 mm", 5, 20],
]


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
    return cantidad


def mostrar_reporte(matriz):
    print("=" * 52)
    print("REPORTE DE REABASTECIMIENTO")
    print("=" * 52)
    print(f"{'Artículo':<30}{'Cantidad a pedir':>22}")
    print("-" * 52)

    articulos_a_pedir = 0
    unidades_totales = 0

    for fila in matriz:
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]

        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"{nombre:<30}{cantidad:>22}")

        if cantidad > 0:
            articulos_a_pedir += 1
            unidades_totales += cantidad

    print("-" * 52)
    print(f"Artículos que necesitan reabastecimiento: {articulos_a_pedir} de {len(matriz)}")
    print(f"Total de unidades a solicitar: {unidades_totales}")


def main():
    mostrar_reporte(inventario)


if __name__ == "__main__":
    main()
