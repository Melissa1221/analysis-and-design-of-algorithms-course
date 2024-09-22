
class Tarea:
    def __init__(self, inicio, fin, beneficio):
        self.inicio = inicio
        self.fin = fin
        self.beneficio = beneficio


def buscar_ultima_no_conflicto(tareas, i):
    for j in range(i - 1, -1, -1):
        if tareas[j].fin <= tareas[i].inicio:
            return j
    return -1


def planificacion_dinamica(tareas):
    # Ordenar tareas según el tiempo de finalización
    tareas.sort(key=lambda x: x.fin)
    
    n = len(tareas)
    dp = [0] * n  
    
    # Inicializar el primer beneficio
    dp[0] = tareas[0].beneficio
    
    
    for i in range(1, n):
        # Beneficio incluyendo la tarea actual
        incl_prof = tareas[i].beneficio
        l = buscar_ultima_no_conflicto(tareas, i)
        if l != -1:
            incl_prof += dp[l]
        
        # El máximo beneficio hasta la tarea i es el máximo entre incluir o excluir la tarea actual
        dp[i] = max(incl_prof, dp[i - 1])
    
    return dp[-1] 


tareas = [
    Tarea(1, 3, 50),
    Tarea(3, 5, 20),
    Tarea(6, 19, 100),
    Tarea(2, 100, 200)
]

resultado = planificacion_dinamica(tareas)
print(f"El beneficio máximo es: {resultado}")
