#iteration && generation
#iteration method: iter() && next()
#generation key: yield

# listCars = ["BMW", "Mercedes", "Bently", "Audi", "Nissan"]
#
# def iterFunc(car):
#     c = car
#     i = iter(c)
#     print(next(i) + " 5 Series M")
#     print(next(i) + "-Benz")
#     print(next(i) + "Motors Limited")
#     print(next(i) + " AG")
#     print(next(i) + " Motor Co., Ltd")
#
# iterFunc(listCars)

# generation
# contacts = {
#     "Nodir": "+998918602711",
#     "Laziz": "+998908002534"
# }
#
# print("Kontaktga odam qo'shish uchun ismi va nomerini kiriting")
#
# userName = input("userName: ")
# userNum = input("phoneNum: +998")
#
# def add_user_func(username, usernum):
#     contacts[username] = "+998" + usernum
#     yield f"{username} kontaktga qo'shildi"
#     yield contacts
#
# result_generator = add_user_func(userName, userNum)
#
# for result in result_generator:
#     print(result)
