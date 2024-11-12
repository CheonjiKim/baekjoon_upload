from collections import deque
N = input()
P = list(map(int, input().split()))
P.sort()

d = deque(P)

sumval = 0
while d:
    sumval += sum(d)
    d.pop()
print(sumval)