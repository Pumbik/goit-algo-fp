import heapq

def dijkstra(graph, start):
    """
    Реалізація алгоритму Дейкстри з використанням бінарної купи.
    
    :param graph: Граф у форматі словника суміжності
    :param start: Початкова вершина
    :return: Словник найкоротших відстаней від start до всіх інших вершин
    """
    # 1. Ініціалізація відстаней: всі нескінченність, початкова - 0
    # Використовуємо словникове включення для всіх вершин графа
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # 2. Створення бінарної купи
    # сортує за першим елементом кортежу
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Вилучаємо вершину з найменшою відстанню (вершина піраміди)
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        # Переглядаємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Додаємо оновлену пару (нова відстань, сусід) у купу
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances


if __name__ == "__main__":
    # Створюємо зважений граф (приклад: карта міст або мережа)
    # A --5--> B --2--> C
    # |        |       ^
    # 10       3       | 4
    # v        v       |
    # D --1--> E ------+
    
    graph_example = {
        'A': {'B': 5, 'D': 10},
        'B': {'A': 5, 'C': 2, 'E': 3},  # Якщо граф ненапрямлений, зв'язки дублюються
        'C': {'B': 2, 'E': 4},
        'D': {'A': 10, 'E': 1},
        'E': {'B': 3, 'C': 4, 'D': 1}
    }

    start_node = 'A'
    print(f"Пошук найкоротших шляхів від вершини '{start_node}':")
    
    shortest_paths = dijkstra(graph_example, start_node)
    
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до вершини {vertex}: {distance}")

    # Перевірка:
    # Шлях A -> B -> C = 5 + 2 = 7
    # Шлях A -> B -> E = 5 + 3 = 8
    # Шлях A -> D -> E = 10 + 1 = 11 (довший, ніж через B)