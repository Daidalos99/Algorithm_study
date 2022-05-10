import random
from timeit import default_timer as timer


class Node(object):                                     # 노드를 생성 및 부모노드 정보를 기억
    def __init__(self, key, parent=None):               # parent는 기본으로 None값
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def insert(node, key):
    if node is None:                                    # 입력한 노드(ex. A, B, C,...)가 없으면 새로운 노드를 생성
        node = Node(key)
    # 입력한 노드가 이미 있을 때
    elif key < node.key:                                # 매개변수 키가 기존 노드의 키값보다 작으면 왼쪽 자식노드로 삽입
        node.left = insert(node.left, key)
        node.left.parent = node
    else:                                               # 매개변수 키가 기존 노드의 키값보다 크면 오른쪽 자식노드로 삽입
        node.right = insert(node.right, key)
        node.right.parent = node
    return node


def delete(node):
    if node.parent is None:
        node = delete_node(node)    # root
    elif node == node.parent.left:
        node.parent.left = delete_node(node)
    else:
        node.parent.right = delete_node(node)


def delete_node(r):
    if r.left is None and r.right is None:
        return None
    elif r.left is not None and r.right is None:
        return r.left
    elif r.left is None and r.right is not None:
        return r.right
    else:
        s = r.right
        while s.left is not None:
            sparent = s
            s = s.left
        r.key = s.key
        if s == r.right:
            r.right = s.right
        else:
            sparent.left = s.right
        return r


root = None
root = insert(root, 50)
insert(root, 99)
insert(root, 78)
insert(root, 57)
insert(root, 80)
insert(root, 4)
insert(root, 64)
insert(root, 35)
insert(root, 58)
insert(root, 33)

print(root.right.left.left.key)
start = timer()
delete(root.right.left.left)
print(timer() - start)
print(root.right.left.left.key)