import heapq

class Node:
    def __init__(self, level, profit, weight, bound, selected_items=None):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
        self.selected_items = selected_items if selected_items is not None else []

    # Definir la comparación de nodos para usar en la cola de prioridad
    def __lt__(self, other):
        return self.bound > other.bound  # Máximo heap basado en el bound

# Calcular el bound del nodo

def calculate_bound(node, number_of_items, items, capacity):
    if node.weight >= capacity:
        return 0  

    bound = node.profit
    total_weight = node.weight
    next_level = node.level + 1

    while next_level < number_of_items and total_weight + items[next_level][0] <= capacity:
        total_weight += items[next_level][0]
        bound += items[next_level][1]
        next_level += 1

    if next_level < number_of_items:
        bound += (capacity - total_weight) * (items[next_level][1] / items[next_level][0])

    return bound

def branch_and_bound_knapsack(items, capacity):
    number_of_items = len(items)
    max_profit = 0
    best_node = None
    priority_queue = []
    root_node = Node(level=-1, profit=0, weight=0, bound=calculate_bound(Node(-1, 0, 0, 0), number_of_items, items, capacity), selected_items=[])
    heapq.heappush(priority_queue, root_node)

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        if current_node.bound > max_profit:
            next_level = current_node.level + 1

            if next_level < number_of_items:
                weight_with_item = current_node.weight + items[next_level][0]
                profit_with_item = current_node.profit + items[next_level][1]
                selected_items_with_item = current_node.selected_items + [next_level]

                if weight_with_item <= capacity and profit_with_item > max_profit:
                    max_profit = profit_with_item
                    best_node = Node(next_level, profit_with_item, weight_with_item, 0, selected_items_with_item)

                bound_with_item = calculate_bound(Node(next_level, profit_with_item, weight_with_item, 0), number_of_items, items, capacity)
                if bound_with_item > max_profit:
                    heapq.heappush(priority_queue, Node(next_level, profit_with_item, weight_with_item, bound_with_item, selected_items_with_item))

                profit_without_item = current_node.profit
                weight_without_item = current_node.weight
                selected_items_without_item = current_node.selected_items

                bound_without_item = calculate_bound(Node(next_level, profit_without_item, weight_without_item, 0), number_of_items, items, capacity)
                if bound_without_item > max_profit:
                    heapq.heappush(priority_queue, Node(next_level, profit_without_item, weight_without_item, bound_without_item, selected_items_without_item))
    return max_profit, best_node.selected_items

# Datos de prueba
items = [(2, 5), (3, 8), (1, 7), (4, 12)]  # (peso, valor)
capacity = 5

# Ejecutar el algoritmo
max_profit, selected_items = branch_and_bound_knapsack(items, capacity)
print(f"El valor maximo obtenido es: {max_profit}")
print(f"Objetos seleccionados: {selected_items}")
