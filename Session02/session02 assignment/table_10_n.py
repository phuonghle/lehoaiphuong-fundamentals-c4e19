# Ask users to enter a number n, then print n x n 1’s and 0’s, consecutively

n = int(input("Enter a number: "))

for i in range(n):
    if i % 2 == 0 :
        for j in range(n):
            if j % 2 == 1:
                print(0, end="  ")
            else:
                print(1, end= "  ")
    else:
        for j in range (n):
            if j % 2 == 0:
                print(0, end="  ")
            else:
                print(1, end="  ")
    print()