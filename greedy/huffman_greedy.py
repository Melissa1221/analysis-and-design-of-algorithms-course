import heapq
class Nodo:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
  
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(simbolos, frecuencias):
    cola = [Nodo(simbolos[i], frecuencias[i]) for i in range(len(simbolos))]
    heapq.heapify(cola)
    while len(cola) > 1:
        nodo1 = heapq.heappop(cola)
        nodo2 = heapq.heappop(cola)
        nuevo_nodo = Nodo(None, nodo1.frecuencia + nodo2.frecuencia)
        nuevo_nodo.izquierda = nodo1
        nuevo_nodo.derecha = nodo2
        heapq.heappush(cola, nuevo_nodo)
    return heapq.heappop(cola)

def generar_codigos(raiz, codigo_actual=""):
    if raiz is None:
        return
    if raiz.simbolo is not None:  # Nodo hoja
        print(f"Símbolo: {raiz.simbolo}, Código: {codigo_actual}")
    generar_codigos(raiz.izquierda, codigo_actual + "0")
    generar_codigos(raiz.derecha, codigo_actual + "1")

def huffman_greedy(simbolos, frecuencias):
    raiz = construir_arbol_huffman(simbolos, frecuencias)
    generar_codigos(raiz)

simbolos = ['a', 'b', 'c', 'd', 'e']
frecuencias = [5, 9, 12, 13, 16]

huffman_greedy(simbolos, frecuencias)
