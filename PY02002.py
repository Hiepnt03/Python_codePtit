fibo = [0,1,1]
for i in range(3,93) :
    tmp = fibo[i-1] + fibo[i-2]
    fibo.append(tmp)
t = int(input())
while t>0:
    t-=1
    a,b = [int(x) for x in input().split()]
    for i in range(a,b+1):
        print(fibo[i],end=' ')
    print('')