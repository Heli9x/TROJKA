def addition(nums):
    sum = 0
    for num in nums:
        sum += int(num)

    return sum


if __name__ == "__main__":
    dataset = list(input())
    print(addition(dataset))