def ToHop(k,n):
    tu, mau = 1,1
    for i in range(n-k+1,n+1):
        tu = tu * i
    for i in range(1,k+1):
        mau = mau * i
    return int(tu/mau)

m = int(input())
arr = []
for i in range(m):
    tmp = str(input()) 
    arr.append(tmp)
n,result = int(0),int(0)
# theo hàng
for i in range(m):
    for j in range(m):
        if arr[i][j] == "C" :
            n +=1
    if n >=2 :
        result = result + ToHop(2,n)
    n = 0
# theo cột
for i in range(m):
    for j in range(m):
        if arr[j][i] == "C" :
            n +=1
    if n >=2 :
        result = result + ToHop(2,n)
    n = 0

print(result)