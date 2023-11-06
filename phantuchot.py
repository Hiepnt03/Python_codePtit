def result(arr):
    n = len(arr)
    count = 0
    max_left = [0]*n
    min_right = [0]*n
    max_left[0] = arr[0]
    for i in range(1,n):
        if arr[i] >= max_left[i-1]:
            max_left[i] = arr[i]
        else:
            max_left[i] = max_left[i-1]
    min_right[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i] <= min_right[i+1]:
            min_right[i] = arr[i]
        else:
            min_right[i] = min_right[i+1]
    if arr[0]<min_right[1]: count+=1
    if arr[n-1]>=max_left[n-2]: count+=1
    for i in range(1,n-1):
        if arr[i]>=max_left[i-1] and arr[i]<min_right[i+1]:
            count+=1
    return count

t = int(input())
while t > 0:
    t-=1
    n = int(input())
    arr = [int(x) for x in input().split()]
    ans = result(arr)
    print(ans)    