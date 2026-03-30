from addition import *
from subtraction import *

def choose_operation():
    operation = input("choose operation:\n[1]-addition\n[2]-subtraction\n[0]-to exit\n:")
    return operation

def enter_numbers():
    numbers = input("enter numbers in the following format [1 12 13] without the '[]', this is the same as 1 + 12 + 13\n:")
    return numbers

def run_calculation():
    while True:
        op = choose_operation()
        if op == "0":
            break
        else:
            nums = enter_numbers()
            result = None
            if op == "1":
                result = addition(nums)

            elif op == "2":
                result = subtraction(nums)

            print(result)