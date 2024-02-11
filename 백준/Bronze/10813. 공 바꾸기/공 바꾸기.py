N, M = map(int, input().split())

baskets = [] 
for i in range(0, N):
    number = i + 1
    baskets.append(number)
    # len(baskets) == N

for iteraton in range(0, M):
    i, j = map(int, input().split())
    start_idx = i - 1
    end_idx = j - 1
    baskets[start_idx], baskets[end_idx] = baskets[end_idx], baskets[start_idx]

for iteraton in range(0, N):
    print(baskets[iteraton], end=" ")