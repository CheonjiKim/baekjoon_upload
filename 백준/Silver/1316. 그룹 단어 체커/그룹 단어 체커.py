N = int(input()) # 100보다 작거나 같은 자연수

def is_grouped(word):
    
    counter_arr = [0] * 26
    
    for i in range(0, len(word)):
        curr_letter = word[i]
        prev_letter = word[i - 1]
        idx = ord(curr_letter) - 97
        if(i == 0):
            # i가 0인 경우를 따로 처리하는 이유는, i - 1이 음수가 되지 않게 하기 위함이다.
            counter_arr[idx] += 1
            continue

    # 문자열을 하나하나 훑는다.
    # 배열 카운트 값이 0이면 그룹이다.
    # 배열 카운트 값이 0보다 크고, 현재 문자가 이전 문자와 같으면 그룹이다.
    # 그 외의 경우는 그룹이 아니다.
        if(counter_arr[idx] == 0):
            counter_arr[idx] += 1
            continue
        elif(counter_arr[idx] > 0 and curr_letter == prev_letter):
            counter_arr[idx] += 1
            continue
        else:
            return False
    return True

count = 0
for i in range(0, N):
    word = input()
    if(is_grouped(word)):
        count += 1
print(count)