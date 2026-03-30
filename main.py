from addition import *
from subtraction import *

hist_list = []
def choose_operation():
    operation = input("choose operation:\n[1]-addition\n[2]-subtraction\n [9]-history\n[0]-to exit\n:")
    return operation

def enter_numbers():
    numbers = input("enter numbers in the following format [1 12 13] without the '[]', this is the same as 1 + 12 + 13\n:")
    return numbers.split(" ")

def log_history(res, op, nums):
    op_dict = {"1":"+", "2":"-"}
    str_op = f"{op_dict[op]}".join(nums)
    hist_str = f"""
        got: {res}
        from: {str_op}
    """
    hist_list.append(hist_str)


def run_calculation():
    while True:
        op = choose_operation()
        if op == "0":
            break
        else:
            result = None
            if op == "1":
                nums = enter_numbers()
                result = addition(nums)
                print(f"Answer is: {result}\n")
                log_history(result, op, nums)



            elif op == "2":
                nums = enter_numbers()
                result = subtraction(nums)
                print(f"Answer is: {result}\n")
                log_history(result, op, nums)

            elif op == "9":
                print("your history: ")
                for hist in hist_list:
                    print(hist)


if __name__ == "__main__":
    run_calculation()