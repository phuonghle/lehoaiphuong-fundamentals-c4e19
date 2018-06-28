from turtle import *


shape("turtle")


n = int(input("Number of sides: "))
for i in range(n):
    forward(100)
    left(360/n)



mainloop()