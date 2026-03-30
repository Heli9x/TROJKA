def addition(nums):
    sum = 0
    for num in nums:
        sum += int(num)

    return sum

""""
This is just an example, remove it if not needed!!! ✌️😎
"""
if __name__ == "__main__":
    dataset = input().split(" ")
    print(addition(dataset))