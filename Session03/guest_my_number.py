from random import *

m = randint(1, 100)
i = 1



# while True:  
while i < 8:
    n = int(input("Guest my number 1 - 100? "))
    if n < m:
        print("Too small")
    elif n == m:
        print("Bingo")
        break
    else:
        print("A little too large")
    i += 1
    if i > 7:
        print("Exceed 7 times") 
