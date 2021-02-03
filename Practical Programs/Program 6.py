# 6. Write a function to find the occurrence of a word in a string.
def word_occurrence(string,word):
    """Returns the number of times the word occured in the given string."""
    string_list=string.split(" ")
    count = 0
    for i in range(0,len(string_list)):
        if string_list[i].startswith(word):
            count+=1
    return count

# Invoking Function
print(word_occurrence("hello ppl hello world","hello"))
print(word_occurrence("Hello World","no"))