import math

count = 0
n,k = [int(x) for x in input().split()]
for i in range(10**(k-1),10**k) :
    if math.gcd(i,n) == 1 :
        if count == 10:
            print("")
            count = 0
        count +=1
        print(i,end=" ")
        