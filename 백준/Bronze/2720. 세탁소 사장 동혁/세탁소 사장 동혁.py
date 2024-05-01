# 1 dollar == 100 cents
# q, d, n, p
# 0.25, 0.1, 0.05, 0.01
# 25, 10, 5, 1


q = 0
d = 0
n = 0
p = 0
testcase = int(input())
for _ in range(testcase):
    change = int(input())
    while(True):
        if(change - 25 >= 0):
            q += 1
            change -= 25
        elif(change - 10 >= 0):
            d += 1
            change -= 10
        elif(change - 5 >= 0):
            n += 1
            change -= 5
        else:
            p = change
            break
    print(q, d, n, p)
    q, d, n, p = 0,0,0,0