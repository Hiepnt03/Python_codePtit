import math


t = int(input())
while t > 0 :
    t -= 1
    a = int(input())
    b = int(str(a)[::-1])
    result = math.gcd(a,b)
    if result == 1 : print("YES")
    else : print("NO")
    