N = int(input())
lines = N * 2 - 1
arr = ["*"] * lines

if (N == 1):
    print("*")
    quit()
elif(N == 2):
    print(" * ")
    print("***")
    print(" * ")
    quit()

for i in range(0, (lines // 2) + 1):
    # 별을 개수대로 배열에 넣는다.
    if (i == 0):
        continue
    arr[i] = arr[lines - i - 1] = "*" * ((2 * i) + 1)

for i in range(0, (lines // 2)):
    # 공백을 개수대로 앞 뒤로 넣는다.
    if (i == 0):
        arr[0] = arr[-1] = " " * (N - i - 1) + arr[i]
        continue
    arr[i] = arr[lines - i - 1] = " " * (N - i - 1) + arr[i]
for i in range(0, len(arr)):
    print(arr[i])