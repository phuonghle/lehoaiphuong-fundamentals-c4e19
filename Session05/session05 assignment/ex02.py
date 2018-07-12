# Write a program to count number occurrences in a list, with AND without using count() function


# cach 1

numbers =[1, 3, 5, 2, 5, 34, 65, 354, 22]
times = 0

finding = True
while finding:

    number_to_find = int(input("Enter a number: "))

    if number_to_find in numbers:
        times = numbers.count(number_to_find)
        print("{0} appears {1} times in my list".format(number_to_find, times))
    else:
        print("{0} is not in my list".format(number_to_find))
        finding = False




