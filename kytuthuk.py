arr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
while t>0:
    ans = ""
    t-=1
    n,k = [int(x) for x in input().split()]
    for i in range(n):
        tmp = ans
        ans = tmp + arr[i] + tmp
    print(ans[k-1])