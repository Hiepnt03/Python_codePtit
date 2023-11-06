a,k,n = [int(x) for x in input().split()]
result = []
x2 = int(n/k)
x1 = int(a/k)
if(x2<x1): print(-1)
else :
    for i in range(x1+1,x2+1):
        result.append(i*k - a)
    if len(result) == 0:
        print(-1)
    else : 
        for i in result:
            print(i,end=" ")
        print()