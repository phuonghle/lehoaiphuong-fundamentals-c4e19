i = -1
flock = [5, 7, 300, 90, 24, 50, 75]
new_flock = flock

# print("Hello, My name is Hiep and here is my sheep sizes: \n", new_flock)

for i in range(-1, 3):
    if i == -1: 
       print("Hello, My name is Hiep and here is my sheep sizes: \n", new_flock)
       print("\n")
    else:
        print("MONTH {0}:".format(i + 1))

        incremented_flock = [x + 50 for x in new_flock]
        print("One month has passed, here is my flock: \n{0}".format(incremented_flock))

        new_flock = incremented_flock

        if i == 2:
            print("\n")
            break


    print("Now my biggest sheep has size {0}, lets sheer it!".format(max(new_flock)))

    new_flock[new_flock.index(max(new_flock))] = 8
    print("After sheering, here is my flock: \n{0}".format(new_flock))

    print("\n")
    
sum_total = sum(new_flock)
print("My flock has size in total: ", sum_total)
print("I would get: {0} * $2 = {1}".format(sum_total, sum_total * 2))


