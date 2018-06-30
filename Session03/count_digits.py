n = int(input("Enter a number: "))
org = n
count = 0
# print(len(n)) -> neu co nhieu so 0 o dau thi co the dem so 0 phia truoc va tru di, nen import Math 


counting = True

# while n//10 > 0:  mac dinh la da chia 1 lan roi nen count = 1
while counting:
    count += 1
    n = n // 10
    if n == 0:
        counting = False

print("{0} has {1} digits".format(org, count))

