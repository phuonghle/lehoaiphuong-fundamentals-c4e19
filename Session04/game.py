# take a word, form random list made from its elements and make ppl guess the original until there are none left


from random import *


word = "champion"
# new = word

m = list(word)

newList = []

i = 0
loop = True 

while loop:
# while i < len(word):
    element_to_del = choice(m)
    # print(element_to_del)
    newList.append(element_to_del)
    m.remove(element_to_del)
    
    if len(m) == 0:
        loop = False

#     n = input("Guest what is the secret word? ")

#     if n == word:
#         print("Correct")
#         break
#     else:
#         print("Try again!")
#         i += 1
#     if i > len(word):
#         loop = False
#         print("Game over")
# # chưa giải quyết đc TH sau khi hết số chữ mà ko đoán đc 






