def FIB(n):
    if f[n] != 0:
        return f[n]
    if n == 0 or n == 1:
        f[n] = 1
    else:
        f[n] = FIB(n-1) + FIB(n-2)
    return f[n]

if __name__ == '__main__':
    value = 10
    f = [0 for i in range(value)]
    for i in range(0, value):
        f[i] = 0
    fibonacci = FIB(value - 1)
    print(fibonacci)