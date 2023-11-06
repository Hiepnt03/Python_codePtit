import math


a,b,c = [int(x) for x in input().split()]
if a == 0 :
    if b==0:
        if c==0:
            print("VSN")
        else :
            print("VN")
    else :
        print("{:.2f}".format(-c/b))
else :
    delta = b*b - 4*a*c
    if delta > 0 :
        print("{:.2f}".format((b+math.sqrt(delta))/(2*a)),"{:.2f}".format((b-math.sqrt(delta))/(2*a)))
    elif delta == 0 :
        print("{:.2f}".format(b/(2*a)))
    else :
        print("VN")