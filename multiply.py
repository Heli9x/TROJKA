#calculator
sign = input()
numbers=[]
result = 0
i=0
while input() != '\n':
    numbers[i] = float(input())
    i += 1
m = 0
if sign == '*' and i >= 2:
    while m < i-1:
        result = numbers[m] * numbers[m+1]
        m += 1
print(result)