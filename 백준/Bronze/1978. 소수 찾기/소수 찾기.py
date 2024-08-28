N = int(input())
arr = list(map(int, input().split()))

not_prime = len(arr)
#print(not_prime)
for e in arr:
    # 1과 합성수를 찾는다.
    if(e == 1):
        not_prime = not_prime - 1
    elif(e == 2):
        pass
    elif(e % 2 == 0):
        not_prime = not_prime - 1
    else:
        #print("curr e;",e)
        for i in range(2, e):
            if(e % i == 0):
                #print("odd but not prime:", e)
                not_prime = not_prime - 1
                break
print(not_prime)

