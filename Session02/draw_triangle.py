# ve hinh tam giac lech
# for i in range(3):
    # nested loop





# cach 1
# for j in range(7):
#     print("* " * (j)) => cach nay nhanh hon, chi co trong python, ko typical
#     j += 1
# print()

# cach 2
n = 5
for i in range(n):
    for j in range(n):
        if (j < n - i - 1):
            print("  ", end="") # thay đổi số space bên trong
        else:
            print("* ", end="")
    # j += 1
    print()