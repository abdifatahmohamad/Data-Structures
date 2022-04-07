# https://www.youtube.com/watch?v=5WZl3MMT0Eg&t=14s

def maxSubArray(nums):
    max_value = float("-inf")
    running_sum = 0
    for n in nums:
        if running_sum < 0:
            running_sum = 0
        running_sum += n
        max_value = max(max_value, running_sum)

    return max_value


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
print(maxSubArray(nums))
