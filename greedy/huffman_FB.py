from itertools import permutations
import heapq


class Nodo:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def generar_arboles_bruta(simbolos, frecuencias):
    n = len(simbolos)
    combinaciones = list(permutations(range(n)))
    mejores_arboles = []

    for combinacion in combinaciones:
        arbol_actual = construir_arbol_bruto(simbolos, frecuencias, combinacion)
        costo_total = calcular_costo(arbol_actual, "", 0)
        mejores_arboles.append((costo_total, arbol_actual))

    mejores_arboles.sort(key=lambda x: x[0])  
    return mejores_arboles[0][1]  


def construir_arbol_bruto(simbolos, frecuencias, combinacion):
    cola = []
    for i in combinacion:
        heapq.heappush(cola, Nodo(simbolos[i], frecuencias[i]))

    while len(cola) > 1:
        nodo1 = heapq.heappop(cola)
        nodo2 = heapq.heappop(cola)
        nuevo_nodo = Nodo(None, nodo1.frecuencia + nodo2.frecuencia)
        nuevo_nodo.izquierda = nodo1
        nuevo_nodo.derecha = nodo2
        heapq.heappush(cola, nuevo_nodo)

    return heapq.heappop(cola)


def calcular_costo(raiz, codigo_actual, costo_acumulado):
    if raiz is None:
        return 0
    if raiz.simbolo is not None:
        return costo_acumulado + raiz.frecuencia * len(codigo_actual)
    return (calcular_costo(raiz.izquierda, codigo_actual + "0", costo_acumulado) +
            calcular_costo(raiz.derecha, codigo_actual + "1", costo_acumulado))


def imprimir_codigos(raiz, codigo_actual=""):
    if raiz is None:
        return
    if raiz.simbolo is not None:
        print(f"Símbolo: {raiz.simbolo}, Código: {codigo_actual}")
    imprimir_codigos(raiz.izquierda, codigo_actual + "0")
    imprimir_codigos(raiz.derecha, codigo_actual + "1")


def huffman_fuerza_bruta(simbolos, frecuencias):
    mejor_arbol = generar_arboles_bruta(simbolos, frecuencias)
    imprimir_codigos(mejor_arbol)


simbolos = ['a', 'b', 'c', 'd', 'e']
frecuencias = [5, 9, 12, 13, 16]

huffman_fuerza_bruta(simbolos, frecuencias)
