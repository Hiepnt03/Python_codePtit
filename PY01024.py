
def check(s) :
    n = len(s)
    sum = 0
    for i in range(n) :
        sum = sum + int(s[i])
    if sum % 10 != 0 : return False
    for i in range(1,n) :
        if abs(int(s[i])-int(s[i-1])) != 2 :
            return False
    return True
t = int(input())
for x in range(t) :
    s = str(input())
    if check(s) : print("YES")
    else : print("NO")