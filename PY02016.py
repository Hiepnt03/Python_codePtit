t = int(input())
while t>0:
    t-=1
    n = int(input())
    arr = {}
    while len(arr)<n:
        arr = [int(x) for x in input().split()]
    arr.sort()
    count = [0]*1000001
    for i in arr:
        count[i] +=1
    Max,index = -1,0
    for i in range(n):
        tmp = Max
        Max = max(Max,count[arr[i]])
        if Max > tmp:
            index = i
    if Max > int(n/2) :
        print(arr[index])
    else :
        print("NO")
    
        
    