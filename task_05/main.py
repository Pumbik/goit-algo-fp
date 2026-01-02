import uuid
import networkx as nx
import matplotlib.pyplot as plt
import collections

#  task 4
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# new

def generate_gradient_colors(n):
    """
    Генерує список з n кольорів у форматі HEX від темного (#1296F0) до світлого.
    """
    colors = []
    # Стартовий колір 
    # Змінимо стартовий на темніший для кращого контрасту
    r_start, g_start, b_start = 0, 50, 100 
    
    # Кінцевий колір (Світло-жовтий/білий RGB)
    r_end, g_end, b_end = 240, 240, 150
    
    for i in range(n):
        # Лінійна інтерполяція
        r = int(r_start + (r_end - r_start) * i / (n - 1))
        g = int(g_start + (g_end - g_start) * i / (n - 1))
        b = int(b_start + (b_end - b_start) * i / (n - 1))
        colors.append(f'#{r:02x}{g:02x}{b:02x}')
    
    return colors

def dfs_iterative(root):
    """
    Обхід в глибину (DFS) використовуючи СТЕК.
    """
    visited_order = []
    if not root:
        return visited_order
    
    # Використовуємо список як стек
    stack = [root]
    
    while stack:
        # LIFO: беремо останній доданий елемент
        node = stack.pop()
        
        visited_order.append(node)
        
        # Додаємо дітей у стек. 
        # Спочатку додаємо ПРАВОГО, щоб ЛІВИЙ був на вершині стека 
        # і оброблявся першим (Root->Left->Right)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return visited_order

def bfs_iterative(root):
    """
    Обхід в ширину (BFS) використовуючи ЧЕРГУ.
    """
    visited_order = []
    if not root:
        return visited_order
    
    # Використовуємо deque як чергу
    queue = collections.deque([root])
    
    while queue:
        # FIFO
        node = queue.popleft()
        
        visited_order.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return visited_order

def visualize_traversal(root, algorithm="dfs"):
    """
    функція для запуску візуалізації.
    """
    # 1. Отримуємо порядок обходу
    if algorithm == "dfs":
        order = dfs_iterative(root)
        title = "DFS (Depth-First Search) - Стек - Темніші відвідуються раніше"
    else:
        order = bfs_iterative(root)
        title = "BFS (Breadth-First Search) - Черга - Темніші відвідуються раніше"
    
    # 2. Генеруємо градієнт кольорів
    total_nodes = len(order)
    colors = generate_gradient_colors(total_nodes)
    
    # 3. Присвоюємо кольори вузлам відповідно до порядку відвідування
    # Перший відвіданий - найтемніший, останній - найсвітліший
    for i, node in enumerate(order):
        node.color = colors[i]
    
    # 4. Малюємо
    draw_tree(root, title)


if __name__ == "__main__":
    # для наочності
    #       0
    #      / \
    #     4   1
    #    / \ / \
    #   5 10 3  2
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)
    root.right.right = Node(2)

    # Запуск візуалізації DFS
    print("Візуалізація DFS (Закрийте вікно графіка, щоб побачити BFS)...")
    visualize_traversal(root, algorithm="dfs")
    
    # Запуск візуалізації BFS
    print("Візуалізація BFS...")
    visualize_traversal(root, algorithm="bfs")