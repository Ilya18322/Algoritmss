import math
import random
from bisect import bisect_left 
import time
import matplotlib.pyplot as plt
import numpy as np

def line_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

def binar_search(array, key):
    
    value = key
    a = array

    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return -1  

    else:
        return mid 
def inter_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    ret = 0
    while array[minimum] < key < array[maximum]:
        mid = int(minimum + (maximum - minimum) * (key - array[minimum]) / (array[maximum] - array[minimum]))
        if array[mid] == key:
            ret = mid
            break
        elif array[mid] > key:
            maximum = mid - 1
        else:
            minimum = mid + 1

    if array[minimum] == key:
        ret = minimum
    if array[maximum] == key:
        ret = maximum
    while ret > 0 and array[ret - 1] == key:
        ret -= 1
    if array[ret] == key:
        return ret 
    else:
        return -1  


def fib_search(array, key):
    x = key
    arr = array
   
    n = len(array)
    fibMMm2 = 0 
    fibMMm1 = 1 
    fibM = fibMMm2 + fibMMm1 
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1;
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    if (fibMMm1 and arr[offset+1] == x):
        return offset+1;
    return -1

def runtime(n, key_dict=0):
    max_time = 0
    arr = np.random.randint(low = 0, high = 100, size = n)
    arr.sort()

    dict = {0: line_search, 1:binar_search, 2:inter_search, 3:fib_search}
    s = 0
    key = 97 #можно изменить на любое целое
    for i in range(50):
        start_time = time.monotonic()
        dict[key_dict](arr, key)
        run = time.monotonic() - start_time
        if i == 0:
            min_time = run
            max_time = run
        else:
            min_time = min(run, min_time)
            max_time = max(run, max_time)
        s += run
    return min_time, s/50, max_time

n = 10
n_count = []
avg = []
mini = []
maximum = []
while n < 1000000:
    result = runtime(n, 3) #менять после проверки одной функции
    n_count.append(n)
    avg.append(result[1])
    maximum.append(result[2])
    mini.append(result[0])
    print(n)
    if n < 100:
        n += 10
    elif n < 1000:
        n += 100
    elif n < 10000:
        n += 1000
    elif n < 100000:
        n += 10000
    else:
        n += 100000

plt.plot(n_count, avg, 'g')
plt.ylabel('Время')
plt.xlabel('Длина массива')
plt.title('Фибоначиев поиск')#меняется на название поиска
plt.tight_layout()
plt.plot(n_count, mini, 'b')
plt.plot(n_count, maximum, 'r')
plt.grid()
plt.savefig('fibon')#меняется на название поиска
