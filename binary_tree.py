import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None: node = Node(key)
    elif key < node.key: node.left = insert(node.left, key)
    else: node.right = insert(node.right, key)
    return node

def search(node, key):
    if node is None or node.key == key: return node
    if key < node.key: return search(node.left, key)
    return search(node.right, key)

x = random.sample(range(5000), 1000)
value = x[800]

root = None
for i in x:
    root = insert(root, i)

print(root.left.right.key)
start = timer()
found = search(root, value)
print(timer() - start)

if found is not Node:
    print('value', value, 'found', found.key) 
    print(True if found.key == value else False)