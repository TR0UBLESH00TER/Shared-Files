# 7.	Write a function to compute the nth Fibonacci number
def FibonacciNum(n):
    n1,n2=0,1
    if n == 1:
        print(n1)
    elif n == 2:
        print(n2)
    else:
        num = 3
        while n>=num:
            temp = n2
            n2 += n1
            n1 = temp
            num +=1
        print(n2)

FibonacciNum(7)
FibonacciNum(8)