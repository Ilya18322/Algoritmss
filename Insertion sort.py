from random2 import randint

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 

N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))

print (arr)

insertion_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])

input()