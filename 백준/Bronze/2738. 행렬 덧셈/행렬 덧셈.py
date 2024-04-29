N, M = map(int, input().split())

matrix_A = []
matrix_B = []
sum_arr = []

# 빈 배열 할당
for i in range(0, N):
    matrix_A.append([])
    matrix_B.append([])
    sum_arr.append([])

# A에 값 입력받기
for i in range(0, N):
    matrix_A[i] = list(map(int, input().split()))

# B에 값 입력받기
for i in range(0, N):
    matrix_B[i] = list(map(int, input().split()))

# 합 구하는 arr를 규격 맞게 채우기
for i in range(0, N):
    for j in range(0, M):
        sum_arr[i].append(0)

# 합 구하는 arr에 합 할당
for i in range(0, N):
    for j in range(0, M):
         sum_arr[i][j] = matrix_A[i][j] + matrix_B[i][j]

for i in range(0, N):
    print(str(sum_arr[i]).strip('[').strip(']').replace(',',''))