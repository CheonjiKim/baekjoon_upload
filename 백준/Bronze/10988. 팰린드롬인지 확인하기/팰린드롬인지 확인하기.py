word = input()
char_arr = []

for letter in word:
    char_arr.append(letter)

length = len(char_arr)
for i in range(0, length):
    if(char_arr[i] == char_arr[length - i - 1]):
        continue
    else:
        print(0)
        quit()
        break
print(1)
