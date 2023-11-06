import math

n = int(input())
arr = [float(x) for x in input().split()]
arr.sort()
minn = arr[0]
maxx = arr[len(arr)-1]
result = []
for i in arr:
    if i != maxx and i!= minn:
        result.append(i)
tbc = 0
for i in result:
    tbc +=i
tbc = tbc/len(result)
print("%.2f"%tbc)