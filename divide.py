def divide(numbers):
    counter = 0
    nums_length = len(numbers)
    result = 1

    while counter < nums_length:
        if counter == 0:
            result = int(numbers[counter])
        else:
            result /= int(numbers[counter])
        counter += 1

    return result