# 6. Write a function to find the occurance of a word in a string
def occurance(check,string):
    L = string.split()
    count = 0
    for i in L:
        if i == check:
            count += 1
    if count == 0:
        print("Word not found")
    else:
        print("The given word occurs",count,"times in the string.")

occurance("hello","hello ppl hello world")
occurance("no","Hello World")
        