t = int(input())
giai_thua = [1,1]
for i in range(2,10):
    giai_thua.append(i*giai_thua[i-1])
while t>0:
    t-=1
    n = int(input())
    sum = 0
    s = str(n)
    for i in s:
        sum = sum + giai_thua[int(i)]
    if sum == n : print("Yes")
    else : print("No")
    