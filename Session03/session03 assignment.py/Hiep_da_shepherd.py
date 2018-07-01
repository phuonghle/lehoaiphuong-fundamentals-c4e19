i = 0
flock = [5, 7, 300, 90, 24, 50, 75]
new_flock = flock

for i in range(4):
    # print("Hello, My name is Hiep and here is my sheep sizes:")
    # print(new_flock)

    # print("Now my biggest sheep has size {0}, lets sheer it!".format(max(new_flock)))

    # new_flock[new_flock.index(max(new_flock))] = 8
    # print("After sheering, here is my flock: \n{0}".format(new_flock))
  
    incremented_flock = [x + 50 for x in new_flock]

    print("One month has passed, here is my flock: \n{0}".format(incremented_flock))
    
    print("\n")

