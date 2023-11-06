import math

def check_snt(n) :
    s = str(n)
    n = 0
    for i in s :
        n = n + int(i)
    if n == 1 : return False
    if n == 2 or n == 3 : return True
    for i in range(2,int(math.sqrt(n)+1)) :
        if n % i == 0 : return False
    return True
    
t = int(input())
while t>0 :
    t -= 1
    a, b = map(int, input().split())
    value = math.gcd(a,b)
    if check_snt(value) : print("YES")
    else : print("NO")
    