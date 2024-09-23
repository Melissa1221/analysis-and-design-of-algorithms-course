import random
import string
import time
import sys
import sys
from typing import List

def generar_subsecuencias(cadena):
    """
    Genera todas las subsecuencias posibles de una cadena dada.
    
    :param cadena: Cadena de entrada
    :return: Lista de todas las subsecuencias
    """
    subsecuencias = ['']  # Incluir la cadena vacía
    for caracter in cadena:
        # Crear nuevas subsecuencias agregando el caracter actual a las existentes
        nuevas_subsecuencias = [sub + caracter for sub in subsecuencias]
        subsecuencias += nuevas_subsecuencias
    return subsecuencias

def es_subsecuencia(s, t):
    """
    Verifica si 's' es una subsecuencia de 't'.
    
    :param s: Subcadena a verificar
    :param t: Cadena principal
    :return: Booleano indicando si 's' es una subsecuencia de 't'
    """
    it = iter(t)
    return all(char in it for char in s)

def lcs_fuerza_bruta(X, Y):
    """
    Encuentra la Subsecuencia Común Más Larga (LCS) usando el método de fuerza bruta.
    
    :param X: Primera cadena
    :param Y: Segunda cadena
    :return: La LCS entre X y Y
    """
    lcs_max = ""
    subsecuencias_X = generar_subsecuencias(X)
    
    for subsecuencia in subsecuencias_X:
        if es_subsecuencia(subsecuencia, Y):
            if len(subsecuencia) > len(lcs_max):
                lcs_max = subsecuencia
                
    return lcs_max

def lcs_programacion_dinamica(X, Y):
    """
    Encuentra la Subsecuencia Común Más Larga (LCS) usando programación dinámica.
    
    :param X: Primera cadena
    :param Y: Segunda cadena
    :return: La LCS entre X y Y
    """
    m = len(X)
    n = len(Y)
    
    # Crear una matriz (m+1) x (n+1) inicializada en 0
    C = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Llenar la matriz C
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i - 1][j], C[i][j - 1])
    
    # Reconstruir la LCS desde la matriz C
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif C[i - 1][j] > C[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()  # La LCS se construye al revés
    return ''.join(lcs)
def generar_cadena(longitud: int, caracteres: str = string.ascii_uppercase) -> str:
    """
    Genera una cadena aleatoria de una longitud dada.

    :param longitud: Longitud de la cadena a generar.
    :param caracteres: Conjunto de caracteres a utilizar para generar la cadena.
    :return: Cadena aleatoria generada.
    """
    return ''.join(random.choice(caracteres) for _ in range(longitud))
def medir_tiempo(func, *args, **kwargs) -> float:
    """
    Mide el tiempo de ejecución de una función dada.

    :param func: Función a medir.
    :param args: Argumentos posicionales para la función.
    :param kwargs: Argumentos con nombre para la función.
    :return: Tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()
    resultado = func(*args, **kwargs)
    fin = time.perf_counter()
    tiempo_ejecucion = (fin - inicio)*1000
    return tiempo_ejecucion, resultado

def main(x,y):
    """
    Funcion principal para generar cadenas, ejecutar metodos de LCS y medir tiempos.
    """
    # Configuración inicial
    longitud_X = x  # Longitud de la primera cadena
    longitud_Y = y  # Longitud de la segunda cadena
    caracteres = string.ascii_uppercase  # Caracteres a utilizar

    X = generar_cadena(longitud_X, caracteres)
    Y = generar_cadena(longitud_Y, caracteres)

    print(f"{longitud_Y} caracteres: {X},{Y}")
    
    # Ejecutar y medir el tiempo del método de fuerza bruta
    #print("Ejecutando Metodo de Programacion Dinamica...")
    tiempo_dinamica, resultado_dinamica = medir_tiempo(lcs_programacion_dinamica, X, Y)
    print(f"LCS (Programacion Dinamica): '{resultado_dinamica}'")
    print(f"Tiempo de ejecucion (Programacion Dinamica): {tiempo_dinamica:.6f} ms")
    
    #print("Ejecutando Metodo de Fuerza Bruta...")
    tiempo_fuerza, resultado_fuerza = medir_tiempo(lcs_fuerza_bruta, X, Y)
    print(f"LCS (Fuerza Bruta): '{resultado_fuerza}'")
    print(f"Tiempo de ejecucion (Fuerza Bruta): {tiempo_fuerza:.6f} ms\n")
    
    
   

if __name__ == "__main__":
    for i in range(1, 21):
        main(i,i)