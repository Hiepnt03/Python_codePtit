t = int(input())
while t>0:
    t-=1
    n = int(input())
    arr_a = [int(x) for x in input().split()]
    arr_b = [int(x) for x in input().split()]
    arr_a.sort()
    arr_b.sort()
    ok = True
    for i in range(n):
        if arr_a[i] > arr_b[i] :
            ok = False
            break
    if ok == True:
        print("YES")
    else: print("NO")