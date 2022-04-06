# https://www.youtube.com/watch?v=MK-NZ4hN7rs

# Fixed size sliding window technique
def max_subArray(nums, k):
    max_value = float("-inf")
    running_sum = 0

    for i in range(len(nums)):
        running_sum += nums[i]
        if i >= k - 1:
            max_value = max(max_value, running_sum)
            running_sum -= nums[i - (k - 1)]
    return max_value


nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3
print(max_subArray(nums, k))
