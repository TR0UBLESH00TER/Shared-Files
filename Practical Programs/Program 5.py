# 5. WAF to check whether a string is palindrome or not
def isPalindrome(String1):
    String2=""
    for i in String1:
        String2 = i+String2
    if String1 == String2:
        print(String1,"is a palindrome.")
    else:
        print(String1,"is not a palindrome.")
isPalindrome("hello")
isPalindrome("racecar")
