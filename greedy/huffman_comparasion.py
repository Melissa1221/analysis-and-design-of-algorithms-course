import time
import heapq
from itertools import permutations
import matplotlib.pyplot as plt
import pandas as pd

# Clase Nodo para ambos enfoques
class Nodo:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# ---- Fuerza Bruta ----

# Construcción de árboles por fuerza bruta
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

def huffman_fuerza_bruta(simbolos, frecuencias):
    mejor_arbol = generar_arboles_bruta(simbolos, frecuencias)
    return mejor_arbol

# ---- Greedy ----

# Construcción del árbol por el método Greedy
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

def huffman_greedy(simbolos, frecuencias):
    raiz = construir_arbol_huffman(simbolos, frecuencias)
    return raiz

# ---- Comparación ----

def medir_tiempo(funcion, simbolos, frecuencias):
    inicio = time.perf_counter()
    funcion(simbolos, frecuencias)
    fin = time.perf_counter()
    return (fin - inicio) * 1000  # tiempo en milisegundos

# Generación de frecuencias y símbolos de prueba de varias longitudes
def generar_datos(n):
    simbolos = [chr(97 + i) for i in range(n)]  # Genera símbolos 'a', 'b', 'c', etc.
    frecuencias = [i+1 for i in range(n)]  # Frecuencias consecutivas
    return simbolos, frecuencias

# Listas para almacenar resultados
resultados = []

# Longitudes de los datos a probar
longitudes = [3, 4, 5, 6, 7, 8, 9, 10]

for longitud in longitudes:
    simbolos, frecuencias = generar_datos(longitud)
    
    # Medir tiempo de ejecución de Fuerza Bruta y Greedy
    tiempo_fuerza_bruta = medir_tiempo(huffman_fuerza_bruta, simbolos, frecuencias)
    tiempo_greedy = medir_tiempo(huffman_greedy, simbolos, frecuencias)
    
    # Guardar resultados
    resultados.append((longitud, tiempo_fuerza_bruta, tiempo_greedy))

# Convertir los resultados en un DataFrame para su visualización
df_resultados = pd.DataFrame(resultados, columns=["Longitud", "Tiempo BF (ms)", "Tiempo Greedy (ms)"])
print(df_resultados)

# Mostrar resultados en formato de tabla
# import ace_tools as tools; tools.display_dataframe_to_user(name="Comparación de tiempos de ejecución", dataframe=df_resultados)

# ---- Gráfica comparativa ----

# Crear la gráfica comparativa
plt.figure(figsize=(10, 6))
plt.plot(df_resultados["Longitud"], df_resultados["Tiempo BF (ms)"], label="Fuerza Bruta", marker='o')
plt.plot(df_resultados["Longitud"], df_resultados["Tiempo Greedy (ms)"], label="Greedy", marker='o')
plt.xlabel("Longitud")
plt.ylabel("Tiempo de Ejecución (ms)")
plt.title("Comparación de Tiempos de Ejecución (Fuerza Bruta vs Greedy)")
plt.legend()
plt.grid(True)

# Mostrar gráfica
plt.show()

