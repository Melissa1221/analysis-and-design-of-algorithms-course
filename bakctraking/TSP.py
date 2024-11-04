import math

# Matriz de distancias entre ciudades (ejemplo con 4 ciudades: A, B, C, D)
distancias = [
    [0, 10, 15, 20],   # Distancias desde A
    [10, 0, 35, 25],   # Distancias desde B
    [15, 35, 0, 30],   # Distancias desde C
    [20, 25, 30, 0]    # Distancias desde D
]

# Función recursiva para encontrar el mínimo costo usando backtracking
def tsp_backtracking(ciudad_actual, visitadas, costo_actual, n, costo_minimo, camino_actual):
    # Si hemos visitado todas las ciudades, regresamos a la ciudad inicial
    if len(visitadas) == n:
        camino_actual.append(0)  # Agregar la ciudad de inicio al final del camino
        return costo_actual + distancias[ciudad_actual][0], camino_actual  # Regresar a la ciudad de inicio

    # Inicializamos el costo mínimo
    mejor_camino = []
    for ciudad in range(n):
        if ciudad not in visitadas:  # Si la ciudad no ha sido visitada
            # Marcamos la ciudad como visitada y avanzamos en el camino
            visitadas.add(ciudad)
            camino_actual.append(ciudad)  # Agregar ciudad al camino
            nuevo_costo, camino = tsp_backtracking(
                ciudad, visitadas, costo_actual + distancias[ciudad_actual][ciudad], n, costo_minimo, camino_actual
            )
            # Actualizamos el costo mínimo si es menor
            if nuevo_costo < costo_minimo:
                costo_minimo = nuevo_costo
                mejor_camino = camino.copy()  # Guardar el mejor camino encontrado
            visitadas.remove(ciudad)  # Retrocedemos (backtracking)
            camino_actual.pop()  # Eliminar la ciudad del camino

    return costo_minimo, mejor_camino

# Llamada inicial al problema del TSP
n = len(distancias)
visitadas = set([0])  # Empezamos en la ciudad 0 (A)
costo_minimo, mejor_camino = tsp_backtracking(0, visitadas, 0, n, math.inf, [0])

print(f"El costo mínimo para completar el recorrido es: {costo_minimo}")
print(f"El camino recorrido es: {mejor_camino}") 