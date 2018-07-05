# write a program to ask user to enter their balance and standardise it

from locale import *

setlocale(LC_ALL, '')

your_balance = int(input("Enter your balance: "))


print("Your updated balance: ",currency(your_balance, grouping=True))
