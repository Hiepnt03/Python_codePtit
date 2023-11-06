import math

def checksnt(n):
    if n < 2: return False
    if n <=3: return True
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def check(s):
    if checksnt(len(s)) == False:
        return False
    count_snt = 0
    for i in s:
        if checksnt(int(i)):
            count_snt +=1
    if count_snt <= len(s) - count_snt :
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