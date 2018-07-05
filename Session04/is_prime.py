



# while loop:
numb = int(input("Enter a number: "))

i = 2

is_prime = True

while i <= (numb ** 0.5):
    if numb % i == 0:
        is_prime = False
        break
    i += 1

if is_prime == True:
    print("{0} is a prime number".format(numb))
else:
     print("{0} is not a prime number".format(numb))
    


# failed01
# loop print + thieu break khien lap nhieu lan 

# n = int(input("Enter a number: "))
# for i in range(2,n - 1):
#     if n % i == 0 and i != n:
#         print("{0} is not a prime number".format(n))
#         i += 1
#     else:
#         print("{0} is a prime number".format(n))
#         break






# count the number of factor: == 2 => prime    




