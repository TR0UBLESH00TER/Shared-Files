# 2. Write a function to accept a number from user and to check whether it is prime or not.
def isPrime(number):
    if number>1:
        for i in range(2,number//2):
            if number%i==0:
                print(number,"is not a prime number.")
                break
        else:
            print(number, "is a prime number.")
    else:
        print(number,"is not a prime number.")

isPrime(3)
isPrime(407)
isPrime(2)
isPrime(35)
