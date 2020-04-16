
from random2 import randint
N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)

    i = 0
    m = i
    j = i + 1

    while j < N:
        if arr[j] < arr[m]:
            m = j
            j += 1
    arr[i], arr[m] = arr[m], arr[i]
 
    i += 1
 
print(arr)