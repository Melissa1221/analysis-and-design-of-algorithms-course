from itertools import combinations

# Clase para representar una tarea
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

tareas = [
    Tarea(1, 3, 50),
    Tarea(3, 5, 20),
    Tarea(6, 19, 100),
    Tarea(2, 100, 200)
]


resultado = planificacion_fuerza_bruta(tareas)
print(f"El beneficio máximo es: {resultado}")
