line_size = 5
str_maxlength = 15

row = []
matrix = []
char_arr = []

# for i in range(0, str_maxlength):
#     row.append('*')

for _ in range(line_size):
    str = input()
    for char in str:
        row.append(char)
    for i in range(len(str), str_maxlength):
        row.append('*')
    matrix.append(row);
    row = []

# print(matrix, len(matrix))

for i in range(str_maxlength):
    for j in range(line_size):
        char_arr.append(matrix[j][i])

# print(char_arr)

sol_arr = []
i = 0

while(i < len(char_arr)):
    if(char_arr[i] != '*'):
        sol_arr.append(char_arr[i])
    i += 1

# print(sol_arr, '\n')
for i in sol_arr:
    print(i, end='')