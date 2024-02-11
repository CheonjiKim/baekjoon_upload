T = int(input())
arr = [""] * T

for i in range(0, T):
    R, S = map(str, input().split())
    R = int(R)

    for letter in S:
        arr[i] += letter*R
        # 문자열에 대해서도 복합증가연산자가 사용 가능하다.

for i in range(0, T):
    print(arr[i])

