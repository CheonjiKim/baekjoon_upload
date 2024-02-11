time_arr = (3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10)
word = input()
total = 0

for letter in word:
    idx = ord(letter) - 65
    total += time_arr[idx]
print(total)