from turtle import *


color("blue")
# speed(-1)


# n = 3
for n in range (7):
    if n%2 == 1:
            color("red")
    else:
        color("blue")
    if n > 2:
        for i in range(n):
            # for j in range(i):
            forward(100)
            left(360/n)







mainloop()