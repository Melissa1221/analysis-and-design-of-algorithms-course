import heapq

def es_valida(pos, laberinto, visitados):
    x, y = pos
    return (0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and
            laberinto[x][y] == 0 and pos not in visitados)

def ramificacion_y_poda(laberinto, inicio, fin):
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio, [inicio]))
    visitados = set()
    mejor_solucion = float('inf')
    mejor_camino = []

    while cola_prioridad:
        distancia, posicion_actual, camino = heapq.heappop(cola_prioridad)
        visitados.add(posicion_actual)
        
        if posicion_actual == fin:
            if distancia < mejor_solucion:
                mejor_solucion = distancia
                mejor_camino = camino
            continue

        for mov in movimientos:
            nueva_posicion = (posicion_actual[0] + mov[0], posicion_actual[1] + mov[1])
            if es_valida(nueva_posicion, laberinto, visitados):
                nueva_distancia = distancia + 1
                if nueva_distancia < mejor_solucion:
                    heapq.heappush(cola_prioridad, (nueva_distancia, nueva_posicion, camino + [nueva_posicion]))

    return mejor_solucion, mejor_camino

# Ejemplo de laberinto
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

inicio = (0, 0)
fin = (4, 4)

# Ejecutar la función y mostrar los resultados
distancia, camino = ramificacion_y_poda(laberinto, inicio, fin)
print(f"La menor distancia es: {distancia}")
print(f"El camino es: {camino}")
