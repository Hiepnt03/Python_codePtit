def check(arr) :
    for i in arr :
        if i != arr[0] :
            return False
    return True

arr = [int(x) for x in input().split()]
while arr != [0,0,0,0] :
    step = 0
    while check(arr) == False :
        tmp_arr = arr.copy()
        arr[0] = abs( tmp_arr[0] - tmp_arr[1] )
        arr[1] = abs( tmp_arr[1] - tmp_arr[2] )
        arr[2] = abs( tmp_arr[2] - tmp_arr[3] )
        arr[3] = abs( tmp_arr[3] - tmp_arr[0] )
        step +=1
    print(step)
    arr = [int(x) for x in input().split()]
            