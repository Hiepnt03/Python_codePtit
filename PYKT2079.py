def cnt(n):
    ans = 0
    s = str(n)
    for i in s:
        if i == '6' or i == '8':
            ans +=1
    return ans
t = int(input())
while t >0:
    t-=1
    n = int(input())
    ans = 0
    for i in range(8,n+1,8):
        ans += cnt(i)
    print(ans)