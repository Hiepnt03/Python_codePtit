def check(A,B):
    if len(A) != len(B):
        return False
    ok = True
    for i in A:
        for j in B:
            if i == j:
                ok = True
                break
            else:
                ok = False
        if ok == False:
            return False
    return True

n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
A = set(a)
B = set(b)
if check(A,B):
    print("YES")
else: print("NO")