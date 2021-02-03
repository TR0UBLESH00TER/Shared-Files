# 8. Write a function to display sum of even number or sum of odd numbers in a list, based on users choice
def sum_odd_or_even(l,choice):
    """Displays sum of even number or sum of odd numbers in a list, based on users choice.
    l is the list and choice is the choice and it can be either "even" or "odd" """
    if choice.lower() not in ("even","odd"):
        print("Choice can have only \"even\" or \"odd\" as value.")
        return
    sum_even = sum_odd = 0
    for i in l:
        if i%2 == 0:
            sum_even+=i
        else:
            sum_odd+=i
    if choice.lower() == "even":
        print(sum_even)
    else:
        print(sum_odd)

# Invoking Function
L=[1,2,3,4]
sum_odd_or_even(L,'Even')
sum_odd_or_even(L,'no')
sum_odd_or_even(L,'Odd')