# # def funksiya
# import random
#
# lFruits = ["olma", "anor", "uzum", "banan"]
#
# randomFruits = random.choice(lFruits)
#
# tahminlar = set()
#
# while True:
#     display = ""
#     for qator in  randomFruits:
#         if qator in tahminlar:
#             display += qator
#         else:
#             display += "_"
#     print(display)
#
#     if "_" not in display:
#         print("siz yutdingiz!")
#         break
#     tahmin = input("tahmin harf: ")
#     tahminlar.add(tahmin)
#     if tahmin not in tahminlar:
#         print("xato")
#     else:
#         print("to'g'ri")
#
#     if len(tahminlar) == 15:
#         print("limit tugadi", "to'g'ri javob esa: ", randomFruits)
#         break
# "use strict"
# import random
#
# cars = ["bmw", "mers", "bently", "bugatti"]
#
# randomAndChois = random.choice(cars)
#
# saveState = set()
#
# while True:
#     grafikDis = ""
#     for latter in randomAndChois:
#         if latter in saveState:
#             grafikDis += latter
#         else:
#             grafikDis += "_"
#             # break
#     print(grafikDis)
#
#     if "_" not in grafikDis:
#         print("ofarin siz yudingiz")
#         break
#     tahmin = input("tahminiy harf: ")
#     saveState.add(tahmin)
#     if tahmin not in grafikDis:
#         print("to'g'ri davom et")
#     else:
#         print("xato o'ylab ko'r")
#
#     if len(saveState) == 15:
#         print("limit tugadi qayta urunib ko'r")
#         break
from itertools import count
from typing import AnyStr

from unicodedata import digit


# Home wor def function

# 1. "user_data" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (first_name, last_name, age).
# Input orqalik ism, familiya va yoshni kiritamiz.
# va bu bu qiymatlarni "user_data" funksiyasini chaqirib argumentlariga beramiz.
# "user_data" funksiyasi bu (first_name, last_name, age) o'zgaruvchilarni qiymatini
#
#   Ism: Alisher
#   Familiya: Olimov
#   Yosh: 27
#
# ko'rinishiga print qilib bersin.

# def user_data(first_name, last_name, age):
#     return f"Your name is: {first_name}, Your surname is: {last_name}, Your age is: {age}"
# print(user_data(first_name="Alisher", last_name="Olimiov", age=27))

# 2. "find_max" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (a, b, c).
# Input orqalik 3 ta son kiritamiz.
# va bu sonlarni "find_max" funksiyasi chaqirib argumentlariga beramiz.
# "find_max" funksiyasini bu (a, b, c) o'zgaruvchilardan eng kattasini
# topib print qiladi.
#
#   Eng katta son - A = 10
#   yoki
#   Eng katta son - A va B = 10
#   yoki
#   Eng katta son - A va B va C = 10

# def find_max(a,b,c):
#     if a > b and c:
#         print(f"Eng katta son - A = {a}")
#     elif a and b > c:
#         print(f"Eng katta son - A va B = {a and b}")
#     elif a and b and c:
#         print(f"Eng katta son - A va B va C = {a and b and c}")
#
#     aNum = input("aNum: ")
#     bNum = input("bNum: ")
#     cNum = input("cNum: ")
#
#     max(aNum, bNum, cNum)
#     if aNum > bNum and cNum:
#         print(f"Eng katta son - A = {aNum}")
#     elif cNum < aNum and bNum:
#         print(f"En katta son - A va B = {aNum and bNum}")
#     elif aNum == bNum == cNum:
#         print(f"Eng katta son - A va B va C = {aNum and bNum and cNum}")
#     else:
#         print("Araqam kichik bo'lishi mumkin emas")
# find_max(10, 10, 10)

# 3. "find_letter_count" funksiyasini elon qilasizlar.
# Funksiyani 2 ta parametri bor (word, letter).
# Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi bolgan so'zimizni kiritamiz.
# va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
# "find_letter_count" funksiyasi bu (word, letter) o'garuvchilardan foydalanib
# "word" da "letter" nechi martda qatnashganini print qilsin.
#
#   "Programing" so'zida "r" dan 2 ta.

# def find_letter_count(words, letter):
#     findWordLetter = words.count(letter)
#     print(findWordLetter)
# find_letter_count(words= "programing", letter= "r")

# 4. "list_sum" funksiyasi elon qilasizlar.
# Funksiyani 1 ta pametrni bor (myList).
# "myList" funksiyasini chaqirib unda argumentini berasizlar.
# uni ichida esa myList elementlarini yig'indisini print qilasizlar.
#
#   Listning elementlar yig'indisi = 32

# def list_sum(myList):
#     num = int(input("num: "))
#     myList.append(num)
#     print(myList)
#     added = sum(myList)
#     print("yig'indisi",added)
# list_sum(myList= [30])

# 5. daraja(a, b) - bu funksiya a ni b darajasini print qilsin

# def daraja(a,b):
#     d2 = b
#     natija = a ** d2
#     print(f"{a} ning {b}-darajasi:", natija)
# daraja(2,4)

# 6. daraja4(a, b, c, d) - bu funksiya a ni b, c va d chi darajasini print qilsin.

# def daraja(a,b,c,d):
#     d1 = b
#     d2 = d
#     natija = a ** b
#     natija2 = c ** d
#     print(f"{a} ning {b}-darajasi va {c} ning {d} darajasi:", natija, ",", natija2)
# daraja(4,4,8,4)

# 7. digit_count_and_sum(word) - bu funksiya "word" ni ichidagi raqamni aniqlab ularni yig'indisini va nechtaligini print qilsin.

# def digit_count_and_sum(word):
#     sumMeth = sum(word)
#     print(sumMeth)
#     countMeth = len(word)
#     print(countMeth)
#
# digit_count_and_sum(word=[4,5,8,15,20])

# 8. add_right(a, b) - bu funksiya a sonini o'ng tomoniga b sonini birlashtirib qoysin va print qilsin.

# def add_right(a, b):
#      addRMeth = str(a) + str(b)
#      print(addRMeth)
# add_right(2,4)

# def add_right(a, b):
#      addRMeth = str(b) + str(a)
#      print(addRMeth)
# add_right(2,4)

# 10. work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga ko'paytirib qiymatini o'zgartiradi va listni print qilsin.

# list = []
#
# def work_with_list(a):
#     minL = min(a)
#     print(minL)
#     for num in a:
#         k = minL * num
#         list.append(k)
#         print(list)
# work_with_list([2,4,8,10])

#
# 11. big_sales(sales) funksiyasini yarating.
# sales bu dictionary:
# {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
#
# qaysi oyda eng ko'p sotuv bolgan bo'lganini return qilsin.

# def big_sales(sales):
#     sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
#     }
#     maxVal = max(sales.values() and sales.keys())
#     maxKey = max(sales.keys() and sales.values())
#     print("mana shu oyda ko'p sotuv bo'lgan", maxVal, maxKey)
# big_sales("sales")

# 12. min_max(numbers, max_num, min_num) max_num numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlang,
# min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang

# def min_max(number, max_num, min_num):
#     veryBigNum = max(number)
#     verySmallNum = min(number)
#
#     if veryBigNum == veryBigNum :
#         print("eng katta son: ",veryBigNum)
#     else:
#         print("eng katta son yo'q")
#     if verySmallNum == verySmallNum:
#         print("eng kichik son: ", verySmallNum)
#     else:
#         print("eng kichik son yo'q")
#
# number = [1,100,1000,10000, 100000,1000000,10000000,100000000,1000000000000000000000000000000]
# max_num = 1000000000000000000000000000000
# min_num = 1
# min_max(number, max_num, min_num)

# 13. expensiveProduct(products) - funksiyadagi products - list.
# Unga products sifatida [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ] shunaqa qiymat beriladi.
# Eng qimmat telefon nomini print qilib bersin bu funksiya.

# def expensiveProduct(products):
#     maxSum = max(products, key=lambda x: x['price'])
#     print(f"Eng qimmat mahsulot: {maxSum['name']}, Narxi: {maxSum['price']}")
#
# products =[
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100}
#     ]
# expensiveProduct(products)



