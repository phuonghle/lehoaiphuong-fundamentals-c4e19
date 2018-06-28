# 10 x 10 1’s and 0’s, consecutively

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i * j, end="  ")
#     print()

for i in range(1, 11):
    for j in range(1, 11):
        # if i < 11:
        if j%2 == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
# for j in range(1, i):
#     if j%2 == 1:
#         print(0, end=" ")
#     else:
#         print(1, end=" ")



# i = 10
# j = 10
# table = [[1 if i%2==0 else 0 for i in range(COLUMNS)] for j in range(ROWS)]

# for row in table:
# for cell in row:
#     print (cell, end=' ')
# print()
