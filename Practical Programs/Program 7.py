# 7. Write a function to compute n terms of Fibonacci numbers.
def Fibonacci(n):
    """Displays till n terms of FIbonacci numbers."""
    n1 = 0
    print(n1,end = " ")
    if n == 1:
        return
    n2 = 1
    print(n2,end = " ")
    if n == 2:
        return
    count = 2
    while True:
        temp = n2
        n2+=n1
        n1 = temp
        count+=1
        print(n2,end = " ")
        if count == n:
            break

# Invoking function
Fibonacci(10)