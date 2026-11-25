# Fase 5 – Evaluación Final POA: Problema 3 (Inventario y reabastecimiento)

Programa en Python que recibe una matriz con el inventario de una bodega y calcula la cantidad exacta que se debe pedir de cada artículo.

## Datos del proyecto

- **Estudiante:** Henry Santiago Buitrago Rojas
- **Curso:** Fundamentos de Programación (213022)
- **Programa:** Ingeniería de Sistemas
- **Universidad:** Universidad Nacional Abierta y a Distancia – UNAD
- **Actividad:** Fase 5 – Evaluación Final POA

## ¿Qué hace el programa?

Cada fila de la matriz `inventario` tiene el formato:

```
[Código, Nombre, Stock actual, Stock mínimo requerido]
```

Para cada artículo se aplica esta regla:

- Si el **stock actual es menor** que el stock mínimo, la cantidad a pedir es `stock mínimo − stock actual`.
- Si el **stock actual es mayor o igual** al stock mínimo, la cantidad a pedir es `0`.

Al final muestra la lista de artículos con su cantidad a pedir, cuántos artículos necesitan reabastecimiento y el total de unidades a solicitar.

## Estructura del código

| Elemento | Función |
|---|---|
| `inventario` | Matriz con los 6 artículos de ejemplo. |
| `calcular_cantidad_a_pedir(stock_actual, stock_minimo)` | Función que devuelve la cantidad exacta a pedir. |
| `mostrar_reporte(matriz)` | Procedimiento que recorre la matriz con un `for` e imprime el reporte. |
| `main()` | Función principal que ejecuta el programa. |

## Cómo ejecutarlo

Requiere Python 3 (no usa librerías adicionales):

```
python Fase5_Problema3_Inventario.py
```

## Ejemplo de salida

```
====================================================
REPORTE DE REABASTECIMIENTO
====================================================
Artículo                            Cantidad a pedir
----------------------------------------------------
Tornillos 1/4 pulgada                              0
Tuercas hexagonales                               45
Arandelas planas                                   0
Cable eléctrico 12 AWG                            40
Cinta aislante                                     0
Brocas de 6 mm                                    15
----------------------------------------------------
Artículos que necesitan reabastecimiento: 3 de 6
Total de unidades a solicitar: 100
```
