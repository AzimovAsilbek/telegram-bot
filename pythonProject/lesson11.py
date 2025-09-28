# while sikll home task
import random
from os import remove
from sys import maxsize

# 1. While siklidan foydalanib print qiling:

# nums1 = 0
#
# while nums1 < 1:
#     nums1 += 1
#     print(nums1)
#
# while nums1 < 22:
#     nums1 +=22 - 1
#     print(nums1)
#
# while nums1 < 333:
#     nums1 += 333 - 22
#     print(nums1)
#
# while nums1 < 4444:
#     nums1 += 4444 - 333
#     print(nums1)
#
# while nums1 < 55555:
#     nums1 += 55555 - 4444
#     print(nums1)
#

# While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.

# print("birinchi qiymatni kiriting!")
# son1 = int(input('son: '))
# print("ikkinchi qiymatni kiriting!")
# son2 = int(input('son: '))
#
# added = son1 + son2
#
# while son1 + son2 :
#     print(added, "javobi")
#     break

# While orqali 1 dan 100 gacha bo'lgan juft solar yig'indisini topuvchi dastur tuzing

# num2 = 0
#
# while num2 < 100:
#     num2 +=1
#     # print(num2)
#     qoldiq = (num2 % 2)
#     # print(qoldiq, "qoldiq")
#
#     if qoldiq == 0:
#         juft = num2 + num2
#         print(num2, 'ni qoldiq', qoldiq, "juft")
#         print("yig'indisi", juft, "juft")
#
#     else:
#         print(num2, 'ni qoldiq', qoldiq, "toq")

# While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing

# num = 0
#
# while num < 100:
#     num += 1
#     # print(num)
#     toq = (num % 2)
#     juft = (num % 2)
#
#     if toq == 1:
#         toqNum = num + num
#         print(num, "toq", "yig'indisi", toqNum)
#
#     if juft == 0:
#         print(num, "juft")


# While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing

# nums = [1,2,3,4,5,6,7,8,9,10]
# smallNum = "kichik raqam"
#
# print("1 dan 10 oralig'idagi raqamlardan birini kiriting!")
#
# forUserVal = int(input('yourValue: '))
#
# numIndex1 = nums[9]
#
# numIndex2 = nums[8]
#
# if forUserVal < numIndex2 or forUserVal < numIndex1:
#     print('')
#
#
# while forUserVal == numIndex1:
#     print("ikkinchi katta raqamni tanladingiz")
#     break
#
# while forUserVal == numIndex2 :
#     print("birinchi katta raqamni tanladingiz")
#     break

# print("1 va 100 oralig'idagi sonlardan birini kiriting!")
#
# while True:
#     userInp = int(input("YourNum: "))
#
#     a = 1
#     b = 100
#
#     ranNum = random.randint(a, b)
#
#     if userInp < ranNum:
#         print("Siz tanlagan son kichik")
#         print("yana urunib ko'ring")
#     else:
#         print("Siz yutdingiz!")
#         break

# While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing

# numbers = [23, 5, 89, 41, 67, 90, 500, 600, 41]
#
# while True:
#     maxNum1 = max(numbers)
#
#     print("birinchi katta raqam: ", maxNum1)
#
#     delMaxNum1 = numbers.remove(maxNum1)
#     break
#
# while True:
#     maxNum2 = max(numbers)
#
#     print("ikkinchi katta raqam: ", maxNum2)
#
#     delMaxNum2 = numbers.remove(maxNum2)
#     break