# make the computer guess correct the number in your mind

print("Guess your number game")
input("Now think of a number from 0 to 100, then press 'Enter'")


print(""" 
'c' if my guess is correct
's' if my guess is smaller than your number
'l' if my guess is larger than your number
""")

low = 0
high = 100

playing = True
while playing:
    mid = (low + high) // 2
    ans = input("Is {0} your number? ".format(mid)).lower()

    if ans == "c":
        print("I knew it!")
        playing = False
    elif ans == "s":
        low = mid   
    elif ans == "l":
        high = mid

    






