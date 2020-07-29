# Finding element in Linear Search:
def linear_search(data, target):
    for i in range(len(data)):
        if target == data[i]:
            return True
    return False

num = [2, 3, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 33]
tar = 28
print(linear_search(num, tar))

# Changed something
#################################################################################
# Finding element in Binary Search iteratively: O(log(n)) time | O(1) space
def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            right = mid -1
        elif target > data[mid]:
            left = mid + 1
    return False

num = [2, 3, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 33]
tar = 28
print(binary_search(num, tar))

#################################################################################
# Finding element in Binary Search recursively: O(log(n)) time | O(log(n)) space
def binary_search_recursively(data, target, left, right):
    if left > right:
        return False
    else:
        mid = (left + right) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursively(data, target, left, mid - 1)
        elif target > data[mid]:
            return binary_search_recursively(data, target, mid + 1, right)
    return False


num = [2, 3, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 33]
tar = 33
print(binary_search_recursively(num, tar, 0, len(num) - 1))
