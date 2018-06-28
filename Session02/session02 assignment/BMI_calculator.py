m = int(input("What is your weight in kg? "))
h = int(input("What is your height in cm? "))


BMI = m / (h/100) ** 2
print("Your BMI is ", BMI)


if BMI < 16:
    print("You are seriously underweight")
elif BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are normal")
elif BMI < 30:
    print("You are overweight")
else: 
    print("You are obese")