# dict methods

# 1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha guruhlaydigan str_counter(strs) funksiya yozing,
# bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
# M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}


# def str_counter(strs):
#     strItem = strs.items()
#     print(strItem)
#     return {
#         len(key): key for key in strs
#     }
#
# dict = {"olma": 1,"shaftoli": 2,"nok":3}
# print(str_counter(dict))

# 2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning
# elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.
# M: list_1 = ["a", "b", "c"]
#    list_2 = [1, 2, 3]
#    merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}

# def merge_list(l1,l2):
#     return {
#         key: value for key,value in zip(l1,l2)
#     }
#
# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# print(merge_list(list_1, list_2))

# 3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish
# imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
# M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}

# contacts = {
#     "Nodir": "+998918602711",
#     "Laziz": "+998908002534"
# }
#
#
# def kontakt_add(name, number):
#     if name in contacts:
#         print(f"{name} ushbu ismli odam kontak da mavjud")
#     else:
#         contacts[name] = number
#         print(f"{name} kontak ga qo'shildi")
#
#
# def update_kontakt(name, number):
#     if name in contacts:
#         contacts[name] = number
#         print("kontakt yangilandi")
#     else:
#         print("kontakt da bunday ism yo'q!")
#
#
# def delet_kontakt(name):
#     if name in contacts:
#         print(f"kontakt dagi {name} o'chirildi")
#     else:
#         print("kontakt da bunday ism yo'q!")
#
#
# def search_kontakt(name):
#     if name in contacts:
#         print(f"{name}: {contacts[name]}")
#     else:
#         print(f"{name} ismli kontakt topilmadi.")
#
#
# def menyu():
#     while True:
#         print("1-kontakt ga odam qo'shish")
#         print("2-kontakt ni yangilash")
#         print("3-kontak dagi odamni o'chirish")
#         print("4-kontakt dan odamni qidirish")
#
#         choice = input("1 dan 4 gacha son kiriting: ")
#
#         if choice == "1":
#             name = input("kontakt ga odam qo'shish uchun ismini kiriting: ")
#             number = input("kontakt ga odam qo'shish uchun telefon raqamini kiriting: ")
#             kontakt_add(name, number)
#         elif choice == "2":
#             name = input("kontaktni yangilash uchun ism kiriting: ")
#             number = input("kontaktni yangilash uchun telefon raqam kiriting: ")
#             update_kontakt(name,number)
#         elif choice == "3":
#             name = input("kontakt dan odamni o'chirish uchun ism kiriting: ")
#             delet_kontakt(name)
#         elif choice == "4":
#             name = input("kontak dan odamni qidirmoqchi bo'lsangiz ismini kiriting: ")
#             search_kontakt(name)
#             break
#         else:
#             print("menyu da bunday raqam berilmagan!")
#
#
# menyu()

# 5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
# o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
# max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }) -> {"Zafar":80, "Nodir":76}

# def max_ball_students(talabalar):
#
#     maxBall1 = max(talabalar, key=talabalar.get)
#     print(f"eng yuqori balni {maxBall1} oldi bali: {talabalar[maxBall1]}")
#     talabalar.pop(maxBall1)
#
#     maxBall2 = max(talabalar, key=talabalar.get)
#     print(f"ikkinchi eng yuqori balni {maxBall2} oldi bali: {talabalar[maxBall2]}")
#
# studentsMaxBall = {
#         "Akmal": 64,
#         "Tohir": 55,
#         "Nodir": 76,
#         "Zafar": 80
# }
# max_ball_students(studentsMaxBall)

dolor = '1$'

print(type(dolor))
