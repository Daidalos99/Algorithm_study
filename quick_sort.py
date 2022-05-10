import random
from timeit import default_timer as timer

def quick_sort(A):
    if len(A) <= 1:
        return A
    x = A[len(A) // 2]
    less = []
    more = []
    equal = []
    for a in A:
        if a < x:
            less.append(a)
        elif a > x:
            more.append(a)
        else:
            equal.append(a)
    return quick_sort(less) + equal + quick_sort(more)

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
print(x)
quick_sort(x)
print(timer() - start)
print(x)
print(test(x))