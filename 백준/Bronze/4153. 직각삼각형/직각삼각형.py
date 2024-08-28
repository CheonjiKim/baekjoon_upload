while(True):
    a, b, c = map(int, input().split())
    if(a == 0 and b == 0 and c == 0):
        break
    arr = [a, b, c]
    max_num = max(arr)
    arr.remove(max_num)
    msg = "right" if (arr[0]**2 + arr[1]**2 == max_num**2) else "wrong"
    print(msg)
    