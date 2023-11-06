t = int(input())
while t>0:
    t-=1
    s = str(input())
    if s[0] == s[-1] :
        print("YES")
    else : print("NO")