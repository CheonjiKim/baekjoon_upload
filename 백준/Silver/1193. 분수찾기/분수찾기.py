# 1/1 을 첫 번째 대각선이라고 하자.
# 1/2와 2/1을 두 번째 대각선이라고 하자.
# 1/3, 2/2, 3/1을 세 번째 대각선이라고 하자.
# 주어진 X가 몇 번째 대각선에 속하는지 찾는다.

X = int(input())

sum = 0
last_sum = 0
k = 1

for i in range(1, 10000000):
    sum += i
    # print("sum value: ", sum)
    if (X <= sum):
        break
    else:
        last_sum = sum
    k += 1

# print("k is: ", k)


bun_mo = []
bun_ja = []

for i in range(1, k + 1):
    bun_ja.append(i)
    bun_mo.append(i)

if(k % 2 == 0):
    bun_mo.reverse()
else:
    bun_ja.reverse()

# print("bunja: ", bun_ja)
# print("bunmo: ", bun_mo)
# print("k is: ", k)
# print("X - last_sum: ", X - last_sum)

idx = X - last_sum - 1
print(f"{bun_ja[idx]}/{bun_mo[idx]}")