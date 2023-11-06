def check(s) :
    for i in range(int(len(s)-1)) :
        if int(s[i]) > int(s[i+1]) :
            return False
    return True
t = int(input())
while t>0 : 
    t -=1
    s = str(input())
    if check(s) : print("YES")
    else : print("NO")
