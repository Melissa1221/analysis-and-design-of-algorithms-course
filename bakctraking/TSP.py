import math

# Matriz de distancias entre ciudades (ejemplo con 4 ciudades: A, B, C, D)
distancias = [
    [0, 10, 15, 20],   # Distancias desde A
    [10, 0, 35, 25],   # Distancias desde B
    [15, 35, 0, 30],   # Distancias desde C
    [20, 25, 30, 0]    # Distancias desde D
]

# Función recursiva para encontrar el mínimo costo usando backtracking
def tsp_backtracking(ciudad_actual, visitadas, costo_actual, n, costo_minimo):
    # Si hemos visitado todas las ciudades, regresamos a la ciudad inicial
    if len(visitadas) == n:
        return costo_actual + distancias[ciudad_actual][0]  # Regresar a la ciudad de inicio

    # Inicializamos el costo mínimo
    for ciudad in range(n):
        if ciudad not in visitadas:  # Si la ciudad no ha sido visitada
            # Marcamos la ciudad como visitada y avanzamos en el camino
            visitadas.add(ciudad)
            nuevo_costo = tsp_backtracking(
                ciudad, visitadas, costo_actual + distancias[ciudad_actual][ciudad], n, costo_minimo
            )
            # Actualizamos el costo mínimo si es menor
            costo_minimo = min(costo_minimo, nuevo_costo)
            visitadas.remove(ciudad)  # Retrocedemos (backtracking)

    return costo_minimo

# Llamada inicial al problema del TSP
n = len(distancias)
visitadas = set([0])  # Empezamos en la ciudad 0 (A)
costo_minimo = tsp_backtracking(0, visitadas, 0, n, math.inf)

print(f"El costo mínimo para completar el recorrido es: {costo_minimo}")
