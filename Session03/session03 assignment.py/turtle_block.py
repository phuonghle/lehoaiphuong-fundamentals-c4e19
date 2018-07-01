from turtle import *

# hay gap error close screen turtle vi wrong range()
speed(-1)



colors = ['red', 'blue', 'brown', 'yellow', 'grey']


i = 0

for i in range(0, len(colors)):
# while i < len(colors) + 1:
    for j in range(2):
        fillcolor(colors[i])
        begin_fill()
        forward(50)
        left(90)
        forward(100)
        left(90)
        end_fill()
    # i += 1
    forward(50)


mainloop()