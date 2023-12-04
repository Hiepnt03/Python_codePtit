t = int(input())
for i in range(t):
    stack = []
    s = str(input())
    max = 1
    for i in s:
        if i == "(" :
            print(max,end=" ")
            stack.append(max)
            max += 1
        if i == ")" :
            print(stack.pop(),end=" ")
    print()