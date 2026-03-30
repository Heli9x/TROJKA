def subtraction(nums):
    difference = int(nums[0])
    for num in range(1, len(nums)):
        difference -= int(num)

    return difference