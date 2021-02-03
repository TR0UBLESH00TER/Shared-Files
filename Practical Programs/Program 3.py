# 3. Write a program remdup(l) to remove duplicates from a list.
def remdup(l):
    """Returns list after removing duplicate values."""
    return_list = []
    for i in l:
        if i not in return_list:
            return_list.append(i)
    return return_list

# Invoking function
print(remdup([1,2,3,2,4,2,5,2,6,1,6,7,7,8,1,9,0]))