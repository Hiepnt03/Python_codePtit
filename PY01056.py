import math

def checksnt(n):
    if n <2 : return False
    if n <=3: return True
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def check(s):
    s = "0" + s
    for i in range(1,len(s),2):
        if int(s[i]) % 2 != 0 :
            return False
    for i in range(2,len(s),2):
        if int(s[i]) % 2 == 0 :
            return False
    sum = 0
    for i in s :
        sum += int(i)
    if checksnt(sum) == False :
        return False
    return True

t = int(input())
while t>0:
    t-=1
    s = str(input())
    if check(s) :
        print("YES")
    else:
        print("NO")