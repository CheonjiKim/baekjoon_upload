# 크기가 100 x 100이고 0으로 채워진 행렬을 만든다.
# 색종이가 놓인 위치에 1을 더한다.

#전체 색종이 넓이에서 값이 0인 구역의 넓이를 뺀다.


width = 100
height = 100
paper_size = 10


# # 100x100이고 0으로 채워진 matrix 만들기
# # 방법 1
# # 이 방법에서 matrix는 row의 메모리 값을 담고 있다.
# # 얕은복사인 것이다. 이걸 이제 알았네...
# row = []
# matrix = []

# for __ in range(width):
#     row.append(0)

# for _ in range(height):
#     matrix.append(row)

# 100x100이고 0으로 채워진 matrix 만들기
# 방법 2
matrix = [[0] * 100 for _ in range(100)] 

# 색종이 덮기
def put_paper2(mtx, x, y):
    x_idx = x - 1
    y_idx = 99 - y

    # 문제에서는 y값이 0부터 위로 올라가는 그림이지만,
    # 파이썬 행은 0th부터 nth까지 내려가는 느낌이다.
    # 이거 구별하는 걸 생각 못해서 1시간 넘게 찾아다님...
    # 90 ... 97 98 99
    for i_ in range(99 - y_idx - 10, 99 - y_idx):
        for j_ in range(x_idx, x_idx + 10):
            mtx[i_][j_] += 1
            # print("해당 위치 값:", mtx[i_][j_]);
            # print("할당좌표: ",i_, j_)




"""
def put_paper(mtx, x, y):
    x_idx = x - 1
    y_idx = y - 1
    for i in range(y_idx, y_idx + paper_size):
        for j in range(x_idx, x_idx + paper_size):
            mtx[i][j] += 1
"""



#입력받기
testcase = int(input())
for _ in range(0, testcase):
    x, y = map(int, input().split())
    put_paper2(matrix, x, y)

#넓이 계산
area = 0
for i in range(0, height):
    for j in range(0, width):
        if (matrix[i][j] > 0):
            #print(i, j, "에서", "종이 있음")
            area += 1

print((area))

'''
testarr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 2):
    for j in range(0, 2):
        testarr[i][j] += 1

print(testarr)

'''

    
    




    



