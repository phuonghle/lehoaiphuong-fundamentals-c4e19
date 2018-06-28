# Ask users to enter a number n, then print n 1’s and 0’s in total consecutively:
n = int(input("Enter the total times: "))


for i in range(n):
    if i%2 == 0:
        print("1 ", end="")
    else:
        print("0 ", end="")


