import random
from timeit import default_timer as timer

def binary_search(x, v):
    start = 0
    end = len(x) - 1
    while start <= end:
        mid = (start + end) // 2
        if x[mid] == v: return mid
        elif x[mid] < v: start = mid + 1
        else: end = mid - 1
    return -1

x = random.sample(range(5000), 1000)
x.sort()
value = x[800]

start = timer()
index = binary_search(x, value)
print(timer() - start)

print('value', value, 'found', index)
print(True if index >= 0 and x[index] == value else False)