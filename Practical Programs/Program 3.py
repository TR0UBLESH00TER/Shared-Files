# 3. Write a Python program  remdup( l ) to remove duplicates from a list
def remdup(l):
    d = {}
    for i in l:
        d[i] = i
    rduplist = []
    for i in d:
        rduplist.append(i) 
    print(rduplist)

remdup(['a','b','a','b','c','c','c','d'])
