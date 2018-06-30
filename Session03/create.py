n = ["toys", "dolls", "bikes"]



print("Hi there! Here are your favorite things so far: {0}".format(n))

# a = input("Name 1 thing you want to add: ")

# n.append(a)

for index, item in enumerate(n):
    print(index + 1, item)   # để hiện từ 1

p = int(input("Position to change: "))
i = input("Thing to change: ")
n[p - 1] = i  # để đếm theo input của customer



# print("Here are your fav. things so far: {0}".format(n))

for index, item in enumerate(n):
    print(index + 1, item)
