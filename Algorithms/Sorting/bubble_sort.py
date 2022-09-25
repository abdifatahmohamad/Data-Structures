def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)

                # Without using swap helper function
                # nums[j], nums[j + 1] = nums[j + 1], nums[j]


def swap(nums, left, right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp


nums = [8, 2, 4, 0, 9, 3]
bubbleSort(nums)
print(nums)
