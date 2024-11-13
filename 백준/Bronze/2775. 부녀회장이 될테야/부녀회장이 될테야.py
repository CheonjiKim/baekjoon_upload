apt = [[n for n in range(15)] for _ in range(15)]

for i in range(1, 15):
    for j in range(0, 16):
        apt[i][j - 1] = sum(apt[i - 1][0:j])

tk = int(input())
for _ in range(tk):
    k = int(input())
    n = int(input())
    print(apt[k][n])
