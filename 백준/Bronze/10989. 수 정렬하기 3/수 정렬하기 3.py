import sys
N = int(sys.stdin.readline().rstrip())
nums = [0 for _ in range(10001)]

for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    nums[number] += 1

for i in range(10001):
    if(nums[i] > 0):
        for _ in range(nums[i]):
            sys.stdout.write(f"{i}\n")