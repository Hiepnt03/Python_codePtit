n = int(input())
while n != 0 :
    result = {n}
    while n != 1 :
        if n % 2 == 0 :
            n = n/2
            result.add(int(n))
        else :
            n = n*3 + 1
            result.add(int(n))
    print(len(result))
    n = int(input())