# decorators

# def dec(f):
#     def nextFunc():
#         print("funksiya chaqirilishidan oldin")
#         f()
#     return nextFunc
#
# @dec
# def func2():
#     print("ikkinchi funksiya ishga tushdi")
# func2()


# def decs(f_funksiyasi):
#     def newFunc(*args, **kwargs):
#         print("yangi funksiyadan oldin")
#         f_funksiyasi(*args, **kwargs)
#     return newFunc
#
# Uname = input("UserName: ")
# @decs
# def decs2(name):
#     print(f"Hello {name}")
# decs2(Uname)