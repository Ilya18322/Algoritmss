from random2 import randint

N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)

left = 0
right = len(arr) - 1

while left <= right:
    for i in range(left, right, +1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    right -= 1

    for i in range(right, left, -1):
        if arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    left += 1

print(arr)