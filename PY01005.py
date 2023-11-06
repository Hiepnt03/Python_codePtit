s = str(input())
num4=0
num7=0
for x in s :
    if x == '4' : num4 += 1
    if x == '7' : num7 += 1
if num4 + num7 == 4 or num4 + num7 == 7 :
    print("YES")
else : print("NO")