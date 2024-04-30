N, M = 9, 9

sum_arr = []
max_value = 0
row_idx = 0
col_idx = 0

# 빈 배열 할당
for i in range(0, N):
    sum_arr.append([])

# 합 구하는 arr를 규격 맞게 채우기
for i in range(0, N):
    for j in range(0, M):
        sum_arr[i].append(0)

row = []
for i in range(0, N):
    row = list(map(int, input().split()))
    sum_arr[i] = row


for i in range(0, N):
    for j in range(0, M):
         if (max_value < sum_arr[i][j]):
             max_value = sum_arr[i][j]
             row_idx = i;
             col_idx = j
             


print(max_value)
print(row_idx + 1, col_idx + 1)