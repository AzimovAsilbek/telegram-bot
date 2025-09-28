#List methods
from functools import reduce
from typing import final

#append method list ni ichiga list qo'shadi yoki element
cars = ["BMW", "Audi", "Merc"]

cars.append("Supra")

print(cars)

#extend method  append bilan bir xil faqat [] belgisiz list qo'shadi
fruits = ['behi', 'xurmo', 'anor']

fruits.extend(['bana', 'kivi', 'apelsen'])

print(fruits)

#count method list ni ichida takrorlangan value larni sonini aniqledi
fruits = ['behi', 'olma', 'banan', 'olma', 'anor']

c = fruits.count('olma')

print(c)

#index method list ni ichidagi value lar ni tartib bilan sanab chiqadi

cars = ['BMW', 'Audi', 'Merc']

i = cars.index('BMW')

print(i)

#pop method  list ni ichidagi value ni olib qoyadi
cars = ['BMW', 'Audi', 'Merc']

p = cars.pop(1)

print(p)
print(cars)

#copy method list ni value sini copy qiladi
cars = ['BMW', 'Audi', 'Merc']

copy = cars.copy()

print(copy)

#insert method list ichidagi qaysidur value dan keyin  qanaqadur value qo'sh deyishimiz mumkin
cars = ['BMW', 'Audi', 'Merc']

cars.insert(2, 'Supra')

print(cars)

#clear method list ni ichini tozaledi
cars = ['BMW', 'Audi', 'Merc']

cars.clear()

print(cars)

#sort method list ni alfabet bo'yicha tartibga soladi
cars = ['BMW', 'Audi', 'Merc']

cars.sort()

print(cars)

#reverse index method list ni value sini tartib son bo'yicha teskari qilib beradi

cars = ['BMW', 'Audi', 'Merc']

cars.reverse()

print(cars)

#reverse alpfabet method list ni value sini alfabet bo'yicha teskari qilib beradi

cars = ['BMW', 'Audi', 'Merc']

cars.sort(reverse=True)

print(cars)

# practice

juft_sonlar = list(filter(lambda x: x % 2 == 0, range(1, 101)))

print(f"juft sonlar yig`indisi: {juft_sonlar}")

juft_sonlar_yigindisi = reduce(lambda x,y: x + y, filter(lambda x: x % 2 == 0, range(1, 101)))

print(f'juft sonlar yig`indisi: {juft_sonlar_yigindisi}')

toq_sonlar = list(filter(lambda x: x % 2 == 1, range(1, 101)))

print(f"toq sonlar: {toq_sonlar}")

toq_sonlar_yigindisi = reduce(lambda x,y: x + y, filter(lambda x: x % 2 == 1, range(1, 101)))

print(f"toq sonlar yig'indisi: {toq_sonlar_yigindisi}")
