import uuid, heapq

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())#  Унікальний ідентифікатор для кожного вузла


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

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def generate_colors(step, nodes_number):
    base_color = [0, 0, 255]
    mul = 255 // nodes_number
    new_color = [base_color[0] + mul * step, base_color[1], base_color[2] - mul * step]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs_visualize(root, nodes_number):
    visited = set()
    stack = [root]
    step = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            node.color = generate_colors(step, nodes_number)
            step += 1
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

def bfs_visualize(root, nodes_number):
    visited = set()
    queue = deque([root])
    node_neighbors = set()
    step = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            node.color = generate_colors(step, nodes_number)
            step += 1
            if node.left is not None:
                node_neighbors.add(node.left)
            if node.right is not None:
                node_neighbors.add(node.right)
            queue.extend(node_neighbors - visited)




# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs_visualize(root, count_nodes(root))

# Відображення дерева
draw_tree(root)
# print(generate_colors(2, 8))

bfs_visualize(root, count_nodes(root))
draw_tree(root)
