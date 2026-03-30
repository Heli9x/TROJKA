#calculator
sign = input()
numbers=[]
i=0
while True:
    x = input()
    if x == '':
        break
    numbers.append(int(x))
    i += 1
m = 0
result = 0
if sign == '-' and i >= 2:
    while m < i:
        if m == 0:
            result = numbers[m]
        else:
            result = result - numbers[m]
        m += 1
print(result)