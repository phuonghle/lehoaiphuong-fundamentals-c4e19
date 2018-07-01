clothes = ["T-Shirt", "Sweater"]
CRUD = ["C", "R", "U", "D"]

while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if n in CRUD:
        if n == "C":
            new_item = input("Enter new item: ")
            clothes.append(new_item)
        elif n == "R":
            print("", end="")
        elif n == "U":
            updated_position = int(input("Update position? "))
            new_item_2 = input("Enter new item: ")
            clothes[updated_position - 1] = new_item_2
        elif n == "D":
            deleted_position = int(input("Delete position? "))
            del clothes[deleted_position - 1]
        print("Our items: ", end="")
        print(*clothes, sep=", ")
        break
    else:
        print("Please try again")
    # break