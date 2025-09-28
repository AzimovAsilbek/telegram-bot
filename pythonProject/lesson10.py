# sikl for and while
from itertools import count

# print('nima ga qiziqasiz')
# user = input('User: ')
#
# if 'kitob' in user or 'kutubxona' in user :
#
#     print("qanay kitob o'qiysiz")
#
#     if 'detektiv' in user:
#
#         print("Sizga Shaytanat kitobini o'qishni maslahat beraman")
#
#     elif 'diniy' in user:
#
#         print("Sizga Hadis va Hayot kitobini o'qishni maslahat beraman")
#
#     if 'sport' in user :
#         print("qaysi sport turiga qiziqasiz")
#
#     if 'futbool' in user:
#
#         print("qaysi kamanda ga muhlislik qilasiz")
#
#         if 'barsa' or 'real':
#
#             print("el-classico ga siz chipta yutub olishingiz mumkin")

# for siklli ro'yxat ni ichidagi elementlarni takrorlash uchun ishledi
# fruits = ["apple", "banana", "orange"]
#
# for fruit in fruits:
#     print(fruit, 'fruit')

# fruitBox = ["apples", "bananas", "oranges"]
#
# forFruitBox = []
#
# for fruit in fruitBox:
#     if fruit not in forFruitBox:
#         forFruitBox.append(fruit)
#         print(forFruitBox)

#while siklli biror shart bajarilganda ishledi shart True yoki False bo'lganida
# num = 0
#
# while num < 100 + 1:
#     print(num)
#     num += 1

# num = 15
#
# a,b = 0,1
#
# for i in range(num):
#     print(a, end= ' ')
#     a,b = b,a + b

# num = 123456789
#
# rnum = ''
#
# for reversed in str(num):
#     rnum = reversed + rnum
#
#     print("teskari raqamlar: ", rnum)

carsList = ["BMW", "MERC", "BENTLY", "MERC", "LAMBORGINI", "FORD"]

massiv = []

if massiv == []:
    massiv.extend(list(set(carsList)))
    print(massiv)

