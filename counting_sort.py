import random
from timeit import default_timer as timer

def counting_sort(A, k):
    B = [0] * len(A)
    C = [0] * (k+1)
    for v in A:
        C[v] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range (len(A)-1, -1, -1):
        v = A[i]
        C[v] -= 1
        B[C[v]] = v
    return B

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.choices(range(50), k=100)     # 0~49범위에서 중복 허용하여 100개
start = timer()

print("Before Sorting: " + str(x) + "\n")
x = counting_sort(x, 49)

print("Processing Time: " + str(timer() - start) + "\n")
print("Sorting Result: " + str(x) + "\n")
print(test(x))