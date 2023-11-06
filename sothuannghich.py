def thuan_nghich(n,k):
    n_str = ''
    while n > 0:
        n_str = str(n % k) + n_str
        n //= k
    return n_str == n_str[::-1]
def count(a,b,m):
    cnt = 0
    for i in range(a,b+1):
        check = True
        for coso in range(2,m+1):
            if not thuan_nghich(i,coso):
                check = False
                break
        if check:
            cnt +=1
    return cnt
a,b,m = [int(x) for x in input().split()]
result = count(a,b,m)
print(result)