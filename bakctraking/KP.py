def knapsack_backtracking(w, v, W):
    n = len(w)
    mejor_valor = [0]
    mejor_solución = []
    solución_actual = []

    def Mochila(i, peso_actual, valor_actual):
        if peso_actual > W:
            return  # Excede la capacidad
        if i == n:
            if valor_actual > mejor_valor[0]:
                mejor_valor[0] = valor_actual
                mejor_solución.clear()
                mejor_solución.extend(solución_actual)
            return

        Mochila(i + 1, peso_actual, valor_actual)

        solución_actual.append(i)
        Mochila(i + 1, peso_actual + w[i], valor_actual + v[i])
        solución_actual.pop()

    Mochila(0, 0, 0)
    return mejor_valor[0], mejor_solución


w = [2, 3, 4, 5]  # Pesos 
v = [3, 4, 5, 6]  # Valores 
W = 9            # Capacidad máxima de la mochila

mejor_valor, mejor_solución = knapsack_backtracking(w, v, W)
print(f"El valor maximo es: {mejor_valor}")
print(f"Los objetos incluidos son: {mejor_solución}")
