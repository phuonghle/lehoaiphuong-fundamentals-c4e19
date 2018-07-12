# (Optional) In Happy Farm, there are initially a couple of rabbits (female and male). 
# This couple of the rabbits reproduces a new couple of rabbits each month. 
# Each newborn rabbit couple becomes mature in one month and then gives a life to a new rabbit couple each month after. 
# Write a program that calculates the number of pair of rabbit after 4 months.


# INCEST AFK =.=

month = 0
pair_lower = 0
pair_higher = 1
no_of_months = 10

while month < no_of_months:
    pair = pair_lower + pair_higher

    print("Month {0}: {1} pair(s) of rabbits".format(month, pair))

    pair_lower = pair_higher
    pair_higher = pair
    month += 1


