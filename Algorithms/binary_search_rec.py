# Binary search algorithm using recursive approach
def find(arr, left, right, target):
    # Base condition (search space is exhausted)
    if left > right:
        return -1

    # Find mid(position) value
    pos = (left + right) // 2

    # Target is found
    if target == arr[pos]:
        return pos

    # Discard all elements in the right search space, including the middle element
    if target < arr[pos]:
        return find(arr, left, pos - 1, target)
    # Discard all elements in the left search space, including the middle element
    else:
        return find(arr, pos + 1, right, target)


arr = [2, 3, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 33]
# arr = [2, 3, 5, 7, 8, 9, 12, 14, 28, 19, 22, 25, 27, 17, 33, 33] # Output -1, left > right
nums = [16, 20, 30, 50, 60, 80, 110, 130, 140, 170]
array = [2, 5, 6, 8, 9, 10]
print(find(arr, 0, len(arr) - 1, 28))
print(find(nums, 0, len(nums) - 1, 140))
print(find(array, 0, len(array) - 1, 5))
