# Bacteria B replicates itself each 2 minutes, write a program that asks users to enter two numbers: 
# the initial B bacteria number and a period of time (in minutes). 
# Calculate and print out the total number of B bacteria after this period.


initial_B = int(input("Enter the initial number of B bacteria: "))

period = int(input("Enter the period of time in minutes: "))


total_B = initial_B * (2 ** (period // 2))


print("There are {0} B bacteria after {1} minutes".format(total_B, period))

