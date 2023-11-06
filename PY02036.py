import math

n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if math.gcd(arr[i],arr[j]) == 1:
            print(arr[i],end=" ")
            print(arr[j])