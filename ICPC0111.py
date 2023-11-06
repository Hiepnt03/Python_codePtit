t = int(input())
while t>0:
    t-=1
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    result = arr[k:] + arr[:k]
    for i in result :
        print(i,end=' ')
    print('')