# https://www.youtube.com/watch?v=MK-NZ4hN7rs
# Dynamically resizable sliding window technique.
def smallest_subArray(target_sum, nums):
    min_value = float("inf")
    running_sum = 0
    window_start = 0

    for i in range(len(nums)):
        running_sum += nums[i]
        while running_sum >= target_sum:
            min_value = min(min_value, i - window_start + 1)
            # Shrinking process
            running_sum -= nums[window_start]
            window_start += 1
    return min_value


nums = [4, 2, 2, 7, 8, 1, 2, 8, 10]  # Smallest_sum >= 8
target_sum = 8
print(smallest_subArray(target_sum, nums))
