N = int(input())

bag_5 = 0

if(N in (4, 7)):
    print(-1)

else:
    bag_5 = N // 5
    remainder = N % 5

    if(remainder == 0):
        print(bag_5)

    if(remainder == 1):
        bag_5 = bag_5 - 1
        print(bag_5 + 2)

    if(remainder == 2):
        bag_5 = bag_5 - 2
        print(bag_5 + 4)

    if(remainder == 3):
        print(bag_5 + 1)

    if(remainder == 4):
        bag_5 = bag_5 - 1
        print(bag_5 + 3)