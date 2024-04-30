dec_values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

N, B = map(str, input().split())
B = int(B);
sum = 0

digit_arr = list(N)
#print(digit_arr)
exp = len(digit_arr) - 1

for i in range(len(digit_arr)):
    sum += dec_values.index(digit_arr[i]) * (B)**exp
    exp -= 1

print(sum)