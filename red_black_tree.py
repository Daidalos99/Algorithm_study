red = 'Red'
black = 'Black'

class Node(object):
    def __init__(self, key, color=red):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


def insert(n, key, color=black):

    if n is None:                       # 입력한 노드(ex. A, B, C,...)가 없으면 새로운 노드를 생성
        n = Node(key, color)
    # 입력한 노드가 이미 있을 때
    elif key < n.key:                   # 매개변수 키가 기존 노드의 키값보다 작으면 왼쪽 자식노드로 삽입
        n.left = insert(n.left, key, color)
        n.left.parent = n
    else:                               # 매개변수 키가 기존 노드의 키값보다 크면 오른쪽 자식노드로 삽입
        n.right = insert(n.right, key, color)
        n.right.parent = n
    return n

def search_node(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search_node(node.left, key)
    else:
        return search_node(node.right, key)


def left_rotate(x):
    global root
    y = x.right
    x.right = y.left
    if y.left != None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y


def right_rotate(x):
    global root
    y = x.left
    x.left = y.right
    if y.right != None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == None:
        root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y


def rb_insert(node, key, color=red):
    insert(node, key, color)
    n = search_node(node, key)
    while n.parent.color == red:                # 부모의 색깔이 빨간색일때(Case 3), 추가된 자식(n)노드는 애초에 빨간색
        if n.parent == n.parent.parent.right:       # 부모가 조부모의 오른쪽 자식일 경우
            u = n.parent.parent.left                    # 왼쪽 자식은 삼촌
            if u.color == red:                            # 삼촌도 빨간색일때
                u.color = black                               # 삼촌: 빨 -> 검
                n.parent.color = black                        # 부모: 빨 -> 검
                n.parent.parent.color = red                   # 조부모: 검 -> 빨
                n = n.parent.parent                         # 현재 자식노드(n)를 새로 추가된 자식에서 조부로를 가리키게 함(그 위에서 또 수정이 일어날 수 있으므로)
            else:                                         # else
                if n == n.parent.left:                      # n이 부모의 왼쪽 자식일 경우
                    n = n.parent                                # n을 p로 교체(회전하기전 미리 교체)
                    right_rotate(n)                             # 반시계 회전
                n.parent.color = black                        # 부모: 빨 -> 검
                n.parent.parent.color = red                   # 조부모: 검 -> 빨
                left_rotate(n.parent.parent)                  # 시계 회전

        else:                                       # 부모가 조부모의 왼쪽 자식일 경우
            u = n.parent.parent.right                   # 오른쪽 자식은 삼촌
            if u.color == red:                            # 삼촌도 빨간색일때
                u.color = black                               # 삼촌: 빨 -> 검
                n.parent.color = black                        # 부모: 빨 -> 검
                n.parent.parent.color = red                   # 조부모: 검 -> 빨
                n = n.parent.parent                         # 현재 자식노드(n)를 새로 추가된 자식에서 조부로를 가리키게 함(그 위에서 또 수정이 일어날 수 있으므로)
            else:                                         # else
                if n == n.parent.right:                     # n이 부모의 오른쪽 자식일 경우
                    n = n.parent                                # n을 p로 교체(회전하기전 미리 교체)
                    left_rotate(n)                              # 시계 회전
                n.parent.color = black                        # 부모: 빨 -> 검
                n.parent.parent.color = red                   # 조부모: 검 -> 빨
                right_rotate(n.parent.parent)                 # 반시계 회전

# 8-1 ppt 46쪽의 기본 노드 구성
if __name__ == '__main__':
    # 예시 트리 추가
    root = Node(61, black)
    insert(root, 52, black)
    insert(root, 85, black)
    insert(root, 76, red)
    insert(root, 93, red)
    # 완성된 트리에 100 삽입
    value = 100
    rb_insert(root, value, red)

    print(root.color)                                       # root(61) 색깔
    print(root.right.color)                                 # 85 색깔
    print(root.right.left.color, root.right.right.color)    # 76, 93 색깔
    print(root.right.right.right.color)                     # 100 색깔

    found = search_node(root, value)

    if found is not Node:
        print('value', value, 'found', found.key)
        print(True if found.key == value else False)