# 8.	Write a function to display sum of even numbers  or sum of odd numbers in a list, based on users choice.
def SumEvenOrOdd(LIST,choice):
    if choice.lower() not in ("even","odd"):
        print("Invalid choice.")
    else:
        SumOdd,SumEven=0,0
        for i in LIST:
            if i%2==0:
                SumEven+=i
            else:
                SumOdd+=i
        if choice.lower()=="even":
            print(SumEven)
        else:
            print(SumOdd)

L=[1,2,3,4]
SumEvenOrOdd(L,'Even')
SumEvenOrOdd(L,'no')
SumEvenOrOdd(L,'Odd')
