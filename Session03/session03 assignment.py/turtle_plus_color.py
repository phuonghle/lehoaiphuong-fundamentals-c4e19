from turtle import *

speed(-1)


colors = ['red', 'blue', 'brown', 'yellow', 'grey']
i = 3
for i in range(3, 7):
# while i < 8:  => cach 2
    for j in range(i):
        forward(100)
        left(360/i)
        color(colors[i - 3])
    # i += 1



mainloop()
