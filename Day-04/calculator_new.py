import sys

def add(num1,num2):
    sum = num1 + num2
    return sum

def sub(num1,num2):
    sub = num1 - num2
    return sub


def mul (num1,num2):
    m = num1 * num2
    return m

def div(num1,num2):
    div = num1 // num2
    return div

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    result = add(num1,num2)
    print(result)

