# 2. WAF to accept a number from user and to check whether it is Prime or not
def Check_Prime(number):
    """Returns True if prime and False if not prime"""
    if number < 2:
        return False

    else:
        for factor in range(2,int((number)**0.5)+1):
            if number % factor == 0:
                return False
        else:
            return True

# Invoking function
print(CheckPrime(123))
print(CheckPrime(1279))
print(CheckPrime(15485863))
print(CheckPrime(153485863))
