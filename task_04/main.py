import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
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


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

#  new
def array_to_heap_tree(array, index=0):
    """
    Рекурсивно перетворює масив (купу) у дерево вузлів Node.
    """
    # Якщо індекс виходить за межі масиву - вузла не існує
    if index >= len(array):
        return None

    # Створюємо вузол з поточного елемента
    node = Node(array[index])

    # Рекурсивно створюємо лівого (2*i + 1) та правого (2*i + 2) нащадків
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = array_to_heap_tree(array, left_index)
    node.right = array_to_heap_tree(array, right_index)

    return node

def draw_heap(heap_array):
    """
    Функція, яка приймає масив купи, будує дерево і малює його.
    """
    if not heap_array:
        print("Купа порожня")
        return

    # 1. Будуємо дерево з масиву
    root = array_to_heap_tree(heap_array)
    
    # 2. Малюємо дерево
    draw_tree(root)



data = [10, 5, 3, 2, 4, 1, 0, 15]
# data = [0, 4, 5, 10, 1, 3]
print(f"Вхідний список: {data}")

heapq.heapify(data)
print(f"Min-Heap (масив): {data}")
# Очікується щось типу: [0, 2, 1, 10, 4, 3, 5, 15]

print("Відображаю купу...")
draw_heap(data)