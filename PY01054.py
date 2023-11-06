t = int(input())
while t>0:
    t-=1
    result = 1
    s = str(input())
    for i in s:
        if i != '0' :
            result = result * int(i)
    print(result)