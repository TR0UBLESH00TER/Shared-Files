# 1. Write a function to find the factorial of a function.
def factorial(number):
    """Returns the factorial of the number."""
    if number == 0:
        return 1
    else:
        product = 1
        while number !=0:
            product *= number
            number -=1
        return product

# Invoking function
print(factorial(5))
print(factorial(10))