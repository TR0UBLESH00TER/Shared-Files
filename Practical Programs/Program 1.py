# 1. WAF to find the factorial of a number.
def factorial(number):
    if number == 0:
        return 1
    else:
        factorial = 1
        for i in range(1,number+1):
            factorial *= i
        return factorial

print(factorial(5),factorial(0),factorial(1))