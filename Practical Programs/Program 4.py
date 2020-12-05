# 4. WAF to search a given word in a string
def FindStr(String,search):
    S = String.split()
    for i in range(len(S)):
        if S[i] == search:
            print("Word found. It is word number",str(i+1)+".")
            break
    else:
        print("Word not found.")

FindStr("If you need help ask google","help")
FindStr("If you need help ask google","python")