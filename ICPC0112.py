import math

def check_snt(n) :
    if n == 1 : return False
    if n == 2 or n ==3 : return True
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i == 0:
            return False
    return True

def solve1(n) :
    if check_snt(n) == False or check_snt(n+2) == False or check_snt(n+6) == False:
        return False
    return True
def solve2(n) :
    if check_snt(n) == False or check_snt(n+4) == False or check_snt(n+6) == False:
        return False
    return True
t = int(input())
while t>0 :
    t-=1
    count = 0
    n = int(input())
    for i in range(2,n-6) :
        if solve1(i) or solve2(i):
            count +=1
    print(count)    