N, M = map(int, input().split())

baskets = [] # len(baskets) == N
for i in range(0, N):
    baskets.append(0)

for iteraton in range(0, M):
    i, j, k = map(int, input().split())
    start_idx = i - 1
    end_idx = j - 1
    for iteraton2 in range(start_idx, end_idx + 1):
        baskets[iteraton2] = k

for iteraton in range(0, N):
    print(baskets[iteraton], end=" ")
    