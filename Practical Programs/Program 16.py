# 16. Write a program to perform operations on stack in python using list.
def isEmpty(S):
    if len(S) == 0:
        return True
    else:
        return False

def Push(S,item):
    global top
    S.append(item)
    top = len(S)-1

def Pop(S):
    global top
    if isEmpty(S):
        return "Underflow"
    else:
        val = S.pop()
        if len(S) == 0:
            top = -1
        else:
            top = len(S)-1
        return val

def Peek(S):
    if isEmpty(S):
        return "Underflow"
    else:
        top = len(S) - 1
        return S[top]

def Show(S):
    if isEmpty(S):
        print("No item in Stack")
    else:
        t = len(S)-1
        print("(Top)",end=" ")
        while t>=0:
            print(S[t],"<=",end=" ")
            t -= 1
        print()

def menu():
    global ch
    print("---- STACK in Python----")
    print("     1. PUSH")
    print("     2. POP")
    print("     3. PEEK")
    print("     4. SHOW STACK")
    print("     0. EXIT")
    ch = int(input("Enter your choice: "))

#Main
S = []
top = None
while True:
    menu()
    if ch == 1:
        val = int(input("Enter Item to Push: "))
        Push(S,val)
    elif ch == 2:
        val = Pop(S)
        if val == "Underflow":
            print("Stack is Empty")
    elif ch == 3:
        val = Peek(S)
        if val == "Underflow":
            print("Stack is Empty")
        else:
            print("Top Item:",val)
    elif ch == 4:
        Show(S)
    elif ch == 0:
        break