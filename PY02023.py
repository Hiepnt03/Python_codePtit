def TongChuSo(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

t = int(input())
while t>0:
    t-=1
    n = int(input())
    arr = [int(x) for x in input().split()]
    my_dict = {}
    for i in arr:
        my_dict[i] = TongChuSo(i)
    my_dict = dict(sorted(my_dict.items(), key=lambda item: (item[1], item[0])))
    for key in my_dict:
        print(key,end=" ")
    print()