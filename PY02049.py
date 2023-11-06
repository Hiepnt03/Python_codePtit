import math

def result(n,p):
    gt_n = 1
    for i in range(1,n+1):
        gt_n *= i
    tmp = int(math.log(gt_n,p)) #logarit cơ số p của n!
    for i in range(tmp,-1,-1):
        if gt_n % (p**i) == 0:
            return i

t = int(input())
while t>0:
    t -=1
    n,p = [int(x) for x in input().split()]
    print(result(n,p))