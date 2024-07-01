N, B = map(int, input().split())
digits = []

while(N // B != 0):
    remainder = N % B
    digits.append(remainder)
    N //= B

remainder = N % B
digits.append(remainder)

digits.reverse()

for i in range(0, len(digits)):
    if (digits[i] > 9 and digits[i] < 36):
        digits[i] + 55
        digits[i] = chr(digits[i] + 55)

digits.append('\n')

for i in range(0, len(digits)):
    print(digits[i], end="")