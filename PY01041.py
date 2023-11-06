def check(s) :
    if len(s) <3 : return False
    tmp,index = 0,0
    for i in range(len(s)):
        tmp = max(tmp,int(s[i]))
        if tmp == int(s[i]) :
            index = i
    for i in range(index) :
        if int(s[i]) >= int(s[i+1]):
            return False
    for i in range(index,len(s)-1):
        if int(s[i]) <= int(s[i+1]):
            return False
    return True

t = int(input())
while t>0 :
    t -= 1
    s = str(input())
    if check(s) : print("YES")
    else : print("NO")