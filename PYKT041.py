import math

def ToHop(k,n):
    if n<k: return 0
    return math.comb(n,k) # C(n,k)

n = int(input())
arr = []
for i in range(n):
    s = str(input())
    arr.append(s)
count,ans = 0,0
# tính theo hàng
for i in range(n):
    for j in range(n):
        if arr[i][j] == "C":
            count +=1
    ans += ToHop(2,count)
    count = 0
# tính theo cột
for i in range(n):
    for j in range(n):
        if arr[j][i] == "C":
            count +=1
    ans += ToHop(2,count)
    count = 0
print(ans)