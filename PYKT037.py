arr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def cosok(n,k):
    result =""
    while n>0:
        if n%k <10:
            result = str( n%k ) + result
        else:
            result = arr[n%k-10] + result
        n = n//k
    return result

t = int(input())
while t>0:
    t-=1
    n,b = [int(x) for x in input().split()]
    print(cosok(n,b))