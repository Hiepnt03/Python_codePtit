def check(s) :
    n = len(s)
    if s[n-2] == '8' and s[n-1] == '6' :
        return True
    else : return False
t = int(input())
for x in range(t) :
    s = str(input())
    if check(s) : print("YES")
    else : print("NO")