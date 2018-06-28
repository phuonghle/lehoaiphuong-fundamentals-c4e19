# Ask user to enter a number n, then print n x n numbers, following multiplication table pattern:



n = int(input('Enter a number: '))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end="  ")
    print()