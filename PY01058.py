import math

def checksnt(s):
    tmp = s[-4] + s[-3] + s[-2] + s[-1]
    n = int(tmp)
    if n <2 : return False
    if n <=3: return True
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

t = int(input())
while t>0:
    t-=1
    s = str(input())
    if checksnt(s) :
        print("YES")
    else:
        print("NO")