def subtraction(nums):
    difference = int(nums[0])
    for num in range(1, len(nums)):
        difference = difference - int(nums[num])
        #print(difference, nums[num])


    return difference