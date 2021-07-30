# Sorting a list in python without sorted function

arr = [5, 2, 4, 1]
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp

            # Same as above code
            # arr[j + 1], arr[j] = arr[j], arr[j + 1]

print(arr)
