# 10 x 10 1’s and 0’s, consecutively

for i in range(1, 10):
    if i % 2 == 0 :
        for j in range(1, 10):
            if j % 2 == 1:
                print(0, end="  ")
            else:
                print(1, end= "  ")
    else:
        for j in range (1, 10):
            if j % 2 == 0:
                print(0, end="  ")
            else:
                print(1, end="  ")
    print()