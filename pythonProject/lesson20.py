# try exept

# emails = ["larrywhells@gmail.com","annomally@gmail.com"]
#
# try:
#     input_for_email = input("email: ")
#     if "@" in input_for_email and "." in input_for_email:
#         emails.append(input_for_email)
#         print(emails)
#     else:
#         print("hato email kiritdingiz")
# except ValueError:
#     print("son kiriting")
#
# users = [
#     {"Ismi": "John", "Xonasi": 12, "Xona turi": "standart"},
#     {"Ismi": "Doe", "Xonasi": 15, "Xona turi": "standart"}
# ]
# rn = ["ekanom", "standart", "lyuks"]
#
# print("\nAstrum mexmon xonasiga hush kelibsiz")
# print("Quyidagi menyu bilan tanishib chiqing")
#
#
# def add_user(name, rnum, rtype):
#     for user in users:
#         if user["Xonasi"] == rnum:
#             print("Bu xona band. Boshqa xona tanlang!")
#             return
#     users.append({"Ismi": name, "Xonasi": rnum, "Xona turi": rtype})
#     print(f"{name} ro'yxatga qo'shildi.")
#
#
# def del_user(name):
#     for user in users:
#         if user["Ismi"] == name:
#             users.remove(user)
#             print(f"{name} ro'yxatdan o'chirildi.")
#             return
#     print("Bunday ism topilmadi!")
#
#
# def show_users():
#     if users:
#         print("\nMehmonlar ro'yxati:")
#         for user in users:
#             print(f"- {user['Ismi']}, Xona: {user['Xonasi']}, Turi: {user['Xona turi']}")
#     else:
#         print("\nMehmonlar ro'yxati bo'sh.")
#
#
# def mAstrum():
#     while True:
#         print("\n1 - Mehmon qo'shish")
#         print("2 - Mehmonni ro'yxatdan chiqarish")
#         print("3 - Mehmonlar ro'yxati")
#         print("0 - Dasturdan chiqish")
#         userInput = int(input("Tanlovingiz: "))
#
#         if userInput == 1:
#             usName = input("Ismi: ")
#             try:
#                 numRoom = int(input("Xona raqami: "))
#             except ValueError:
#                 print("Iltimos, xona raqamini to'g'ri kiriting!")
#                 continue
#
#             while True:
#                 print("Xona turlari:")
#                 print("ekanom")
#                 print("standart")
#                 print("lyuks")
#
#                 roomn = input("Xona turini tanlang: ")
#                 if roomn in rn:
#                     add_user(usName, numRoom, roomn)
#                     break
#                 else:
#                     print("Noto'g'ri xona turi tanlandi!")
#
#
#         elif userInput == 2:
#             delet = input("ismi: ")
#             del_user(delet)
#
#         elif userInput == 3:
#             show_users()
#
#         elif userInput == 0:
#             print("Dasturdan chiqildi.")
#             break
#
#         else:
#             print("Noto'g'ri tanlov.")
#
#
# mAstrum()
