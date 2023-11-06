n, m = [int(x) for x in input().split()]
a = [[]]*50
Min, Max = 10**6, 0
for i in range(n):
    a[i] = [int(x) for x in input().split()]
    Min = min(Min, min(a[i]))
    Max = max(Max, max(a[i]))
ok = 0
x = Max-Min
for i in range(n):
    for j in range(m):
        if a[i][j] == x:
            ok = 1
if ok == 0:
    print("NOT FOUND")
else:
    print(x)
    for i in range(n):
        for j in range(m):
            if a[i][j] == x:
                print("Vi tri [", i, "][", j, "]", sep="")