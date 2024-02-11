N = int(input())
arr = [""] * N
for i in range(0, N):
    word = input()
    arr[i] = word[0] + word[-1]

for i in range(0, N):
    print(arr[i])