from turtle import *


color("blue")
speed(-1)

k = 0

for i in range(50):
    for j in range(4):
        forward(i + k)
        left(90)
    left(10)
    i += 1
    k += 1



mainloop()