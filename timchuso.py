import math


t = int(input())
for i in range(1,t+1):
    n = int(input())
    result = str(int(math.pow(3+math.sqrt(5),n)))
    if len(result) < 2:
        print("Case #"+str(i)+": 00" + result)
    elif len(result) <3:
        print("Case #"+str(i)+": 0" + result)
    else:
        print("Case #"+str(i)+": " + result[-3] + result[-2]+result[-1])