import time
from itertools import combinations
import pandas as pd
import matplotlib.pyplot as plt


class Tarea:
    def __init__(self, inicio, fin, beneficio):
        self.inicio = inicio
        self.fin = fin
        self.beneficio = beneficio


def no_hay_conflictos(subconjunto):
    for i in range(len(subconjunto)):
        for j in range(i + 1, len(subconjunto)):
            if subconjunto[i].fin > subconjunto[j].inicio:
                return False
    return True


def sumar_beneficio(subconjunto):
    return sum(tarea.beneficio for tarea in subconjunto)


def planificacion_fuerza_bruta(tareas):
    n = len(tareas)
    max_beneficio = 0
    
    
    for r in range(1, n + 1):
        for subconjunto in combinations(tareas, r):
            if no_hay_conflictos(subconjunto):
                beneficio = sumar_beneficio(subconjunto)
                max_beneficio = max(max_beneficio, beneficio)
    
    return max_beneficio

# Programación Dinámica


def buscar_ultima_no_conflicto(tareas, i):
    for j in range(i - 1, -1, -1):
        if tareas[j].fin <= tareas[i].inicio:
            return j
    return -1

def planificacion_dinamica(tareas):

    tareas.sort(key=lambda x: x.fin)
    
    n = len(tareas)
    dp = [0] * n  
    
   
    dp[0] = tareas[0].beneficio
    
   
    for i in range(1, n):
       
        incl_prof = tareas[i].beneficio
        l = buscar_ultima_no_conflicto(tareas, i)
        if l != -1:
            incl_prof += dp[l]
        
        
        dp[i] = max(incl_prof, dp[i - 1])
    
    return dp[-1]  

def medir_tiempos(tareas):
    # Medir tiempo para Fuerza Bruta
    start_fb = time.time()
    max_beneficio_fb = planificacion_fuerza_bruta(tareas)
    end_fb = time.time()
    
    # Medir tiempo para Programación Dinámica
    start_dp = time.time()
    max_beneficio_dp = planificacion_dinamica(tareas)
    end_dp = time.time()
    
  
    return (end_dp - start_dp) * 1000, (end_fb - start_fb) * 1000  # En milisegundos

# Generar tareas aleatorias para longitudes variadas
longitudes = list(range(1, 21))
resultados = []

for longitud in longitudes:
    tareas = [Tarea(i, i + 2, i * 10) for i in range(1, longitud + 1)]
    tiempo_dp, tiempo_fb = medir_tiempos(tareas)
    resultados.append((longitud, tiempo_dp, tiempo_fb))

# Crear DataFrame con los resultados
df = pd.DataFrame(resultados, columns=["Longitud", "Tiempo DP (ms)", "Tiempo BF (ms)"])

# Mostrar los resultados en formato de tabla en la terminal
print(df.to_string(index=False))

# Graficar los tiempos de ejecución usando matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df["Longitud"], df["Tiempo DP (ms)"], label="Tiempo DP (ms)", marker='o', color='blue')
plt.plot(df["Longitud"], df["Tiempo BF (ms)"], label="Tiempo BF (ms)", marker='o', color='red')
plt.xlabel("Longitud de las Tareas")
plt.ylabel("Tiempo de Ejecución (ms)")
plt.title("Comparación de Tiempos de Ejecución: Programación Dinámica vs Fuerza Bruta")
plt.legend()
plt.grid(True)
plt.show()
