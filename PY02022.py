import math


def checksnt(n):
    if n <2: return False
    if n <=3: return True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True
    
n = int(input())
arr = [int(x) for x in input().split()]
arr2 = []
for i in arr:
    if checksnt(i) and i not in arr2:
        arr2.append(i)
for i in arr2:
    if checksnt(i):
        print(i,end=" ")
        print(arr.count(i))