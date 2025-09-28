#OOP Class va methods
from pythonProject.lesson10 import carsList


class Osson1:
    a = 15

    def __init__(self):
        self.output_a(self.a)

    def output_a(self, a):
        print(f"aning qiymati {a}")

# obj = Osson1()

class Osson2:
    a = 10
    b = 5

    def __init__(self):
        self.summa(self.a, self.b)

    def summa(self, a, b):
        add = f"a va b ning yig'indisi: {a} + {b}"
        print(add)

# obj2 = Osson2()

class Osson3:
    a = -7
    thero = 0

    def __init__(self):
        self.plus_minus(self.a, self.thero)

    def plus_minus(self, a, thero):
        if a > thero:
            print(f"{a} manfiy son")
        else:
            print(f"{a} musbat son")

# obj3 = Osson3()

class Oson4:
    a = 7
    two = 2

    def __init__(self):
        self.odd_even(self.a, self.two)

    def odd_even(self, a, two):
        b = a / two
        if b == 0:
            print(f"{a} juft son")
        else:
            print(f"{a} toq son")

# obj4 = Oson4()

class Osson5:
    a = 7
    b = 3

    def __init__(self):
        self.daraja(self.a, self.b)

    def daraja(self, a, b):
        d = a ** b
        print(f"a va b ning darajasi {d}")

# obj = Osson5()

class MyClass6:
    words = []

    def __init__(self):
        self.add_word(self.words, "BodyBuilder")

    def add_word(self, words, word):
        words.append(word)
        print(words)


# obj6 = MyClass6()

class MyClass7:
    def __init__(self):
        self.myDict = {}

    def add_elem(self, key, val):
        if key not in self.myDict:
            self.myDict[key] = val

    def update_elem(self, key, val):
        if key in self.myDict:
            self.myDict[key] = val

# obj7 = MyClass7()
#
# obj7.add_elem("a", 10)
# print(obj7.myDict)
# obj7.add_elem("a", 20)
# print(obj7.myDict)
#
# obj7.update_elem("a", 30)
# print(obj7.myDict)
# obj7.update_elem("a", 40)
# print(obj7.myDict)
# obj7.update_elem("a", 50)
# print(obj7.myDict)
# obj7.update_elem("a", 60)
# print(obj7.myDict)

class MyClass8:
    def __init__(self):
        self.numbers = [1,2,3,4,5,6,7,8,90]

    def compare_lists(self,new_list):
        sumM = sum(self.numbers)
        print(f"birimchi listdagi raqamlar yig'indisi: {sumM}")
        sumM2 = sum(new_list)
        print(f"ikkinchi listdagi raqamlar yig'indisi: {sumM2}")

        maxListnum = max(sumM, sumM2)

        if sumM > sumM2:
            print(f"birinchi list eng kattasi {maxListnum}")
        else:
            print(f"ikkinchi list eng kattasi {maxListnum}")

# obj8 = MyClass8()
#
# new_mass = [1,2,3,4,5,6,7,8,9,10]
# obj8.compare_lists(new_mass)


class MyClass9:
    list1 = [10, 46, 87, 34, 98, 29]
    list2 = [1, 64, 87, 104, 89, 23]

    def __init__(self):
        self.list1, self.list2

    def list1_max(self):
        maxNum = max(self.list1)
        print(f"list1 dagi maximum son: {maxNum}")

    def list2_max(self):
        maxNum2 = max(self.list2)
        print(f"list2 dagi maximum son: {maxNum2}")

    def sum_of_two_max(self):
        added = max(self.list1) + max(self.list2)
        print(f"\nlistdagi ikkita maximum sonlarni yig'indisi: {added}")

# obj9 = MyClass9()
#
# obj9.list1_max()
# obj9.list2_max()
# obj9.sum_of_two_max()

class MyClass10:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self):
        self.numbers = MyClass10.numbers

    def divid(self, d):
        for n in self.numbers:
            b = n % d
            if b == 0:
                print(f"{n} soni {d} ga qoldiqsiz bo'linadi")

# obj10 = MyClass10()
# obj10.divid(2)