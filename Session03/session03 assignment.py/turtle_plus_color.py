from turtle import *

color("red")
speed(-1)

# speed(-1)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# i = 3
# for i in range(3, 7):
while i < 8:
    for j in range(i):
        forward(100)
        left(360/i)
        color(colors[i])



mainloop()
