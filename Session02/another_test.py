yob = int(input("What is your birth year? "))


age = 2018 - yob


# print("Your age: ", age)


# CONDITIONAL STATEMENTS
if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
else: # khong co condition sau else
    print("Not Baby")
print("Bye")