# 2. WAF to accept a number from user and to check whether it is Prime or not
def Check_Prime(number):
    """Returns True if prime and False if not prime"""
    if number == 1:
        return False # 1 is Neither Prime nor Composite
    elif number in (2,3):
        return True
    else:
        for i in range(2,int((number**0.5))+1):
            if number % i == 0:
                return False
                break
        else:
            return True

# Invoking function
print(Check_Prime(123))
print(Check_Prime(1279))