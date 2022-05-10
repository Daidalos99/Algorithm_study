k = [[6,    7,    12,    5],
     [5,    3,    11,   18],
     [7,   17,     3,    3],
     [8,   10,    14,    9]]

def make_Matrix(a, b):
    return [[0 for _ in range(b)] for i in range(a)]

def Matrix_Path(a, b):
    for i in range(1, a):
        for j in range(1,b):
            c[i][j] = k[i-1][j-1] + max(c[i-1][j], c[i][j-1])
    return c[a-1][b-1]

if __name__ == '__main__':
    m, n = 4, 4
    a, b = m + 1, n + 1
    c = make_Matrix(a,b);
    print(c)
    print(Matrix_Path(a, b))
