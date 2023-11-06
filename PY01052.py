import math
def check(n):
    if n <= 1:
        return False
    elif n<=3:
        return True
    else:
        for i in range(2,int(math.sqrt(n))):
            if n % i == 0:
                return False
    return True

t = int(input())
while t>0:
    t-=1
    s = str(input())
    sum = 0
    for i in s:
       sum += int(i)
    if check(sum):
        print("YES")
    else:
        print("NO")