# 97, 122 => a to z
S = input()
arr = [-1]*(122 - 97 + 1)
idx = 0
for j in range(97, 122 + 1):
    arr[idx] = S.find(chr(j))
    idx = idx + 1

for i in range(0, len(arr)):
    print(arr[i], end=" ")