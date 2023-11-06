t = int(input())
while t > 0:
    t -=1
    ok = True
    n = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A.sort()
    B.sort()
    for i in range(n) :
        if A[i] > B[i]:
            print("NO")
            ok = False
            break
    if ok == True:
        print("YES")