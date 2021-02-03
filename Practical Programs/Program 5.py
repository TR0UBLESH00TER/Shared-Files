# 5. Write a function to whether a string is palindrome or not.
def Check_Palindrome(string):
    """Returns reversed string."""
    reverse_string = ""
    for i in string:
        reverse_string = i+reverse_string
    if reverse_string == string:
        return True
    else:
        return False

# Invoking Function
print(Check_Palindrome('level'))
print(Check_Palindrome('python'))