n = int(input())
a = [int(x) for x in input().split()]
a.sort()
x = max( a[0]*a[1], a[-1]*a[-2])
y = max( a[0]*a[1]*a[-1], a[-1]*a[-2]*a[-3])
ans = max(x, y)
print(ans)