room_num = int(input())
counter = 1
total = 1

while(True):
    if(room_num == 1):
        print(counter)
        break
    
    total = (6 * counter) + total
    #print("curr total: ", total)
    counter += 1

    if(room_num <= total):
        print(counter)
        break
