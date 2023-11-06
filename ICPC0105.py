t = int(input())
while t>0 :
    t -=1
    s = str(input())
    tmp = 0
    my_set = []
    for i in s:
        if i >="0" and i <= "9":
            tmp = tmp*10 + int(i)
        else:
            my_set.append(tmp)
            tmp = 0
    my_set.sort()
    print(my_set[len(my_set)-1])