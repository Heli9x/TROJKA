from addition import *
from subtraction import *
from divide import *

def choose_operation():
    operation = input("choose operation:\n[1]-addition\n[2]-subtraction\n[3]-division\n[4]-multiply\n[9]-history\n[0]-to exit\n:")
    return operation

def enter_numbers():
    numbers = input("enter numbers in the following format [1 12 13] without the '[]', this is the same as 1 + 12 + 13\n:")
    return numbers.split(" ")

hist_list = []
def log_history(res, op, nums):
    op_dict = {"1":"+", "2":"-", "3":"/", "4":"x"}
    str_op = f" {op_dict[op]} ".join(nums)
    hist_str = f"""
        got: {res}
        from: {str_op}
    """
    hist_list.append(hist_str)

def run_calculation():
    while True:
        op = choose_operation()
        if op in ["0", "9"]:
            if op == "0":
                break
            elif op == "9":
                print("your history: ")
                for hist in hist_list:
                    print(hist)

        elif op in ["1", "2", "3", "4"]:
            nums = enter_numbers()
            result = None

            if op == "1":
                result = addition(nums)

            elif op == "2":
                result = subtraction(nums)
            
            elif op == "3":
                result = divide(nums)

            print(f"Answer is: {result}\n")    
            log_history(result, op, nums)


if __name__ == "__main__":
    run_calculation()