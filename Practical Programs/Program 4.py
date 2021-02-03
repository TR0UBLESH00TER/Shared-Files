# 4. Write a function to search a given word in a string.
def search_word(string,word):
    """Searchs word in a string and returns if place with 1 as first word and so on."""
    string_list=string.split(" ")
    for i in range(0,len(string_list)):
        if string_list[i].startswith(word):
            print(f"Word found. It is at place {i+1} in the string.")
            break
    else:
        print("Word not found.")

# Invoking function
search_word("Python is an interpreted, high-level and general-purpose programming language.","Python")
search_word("Python is an interpreted, high-level and general-purpose programming language.","Java")