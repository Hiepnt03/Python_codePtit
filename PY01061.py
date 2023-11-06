import math
def checksnt(n):
    if n <2 : return False
    if n <=3: return True
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
def check(s):
    tmp1 = s[-3] + s[-2] + s[-1]
    tmp2 = s[0] + s[1] + s[2]
    if checksnt(int(tmp1)) and checksnt(int(tmp2)):
        return True
    else:
        return False

t = int(input())
while t>0:
    t-=1
    s = str(input())
    if check(s) :
        print("YES")
    else:
        print("NO")