#recursev function
from itertools import chain

#factorila

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(4))

#fibanacci berilgan son dan avvalgi ikkita sonni yig'indisiga teng

# word = int(input("febanacci: "))
# def febanacci(n, cache={}):
#     if n in cache:
#         return cache[n]
#     if n == 0:
#         return  0
#     elif n == 1:
#         return  1
#     else:
#         result = febanacci(n - 1) + febanacci(n - 2)
#     cache[n] = result
#     return result
# print(febanacci(word))

# numsList = [2, 5, 1, 3, 4, 8, 6, 7, 10, 9]
#
#
# def quick_sort(mass):
#     if len(mass) <= 1:
#         return mass
#     else:
#         p = mass[0]
#         l = [lx for lx in mass[1:] if lx <= p]
#         r = [rx for rx in mass[1:] if rx > p]
#
#         return quick_sort(l) + [p] + quick_sort(r)
#
#
# print(quick_sort(numsList))
