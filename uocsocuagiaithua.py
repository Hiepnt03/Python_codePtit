def result(n,p):
    x = 0
    while n>=p:
        n //= p
        x += n
    return x
t = int(input())
while t>0:
    t -=1
    n,p = [int(x) for x in input().split()]
    print(result(n,p))