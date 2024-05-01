N = int(input())

arr = []
value = 2
arr.append(value**2)
for i in range(0,15):
    arr.append((2*value-1)**2)
    value = (2*value-1)

print(arr[N])