a = 20
b = a ** 2 #a ning kvadrat darajasi ni topdim
print('salom dunyo', b)

c = [1,2,4,5,6]
print(c[2])

dict = {
    "ims": "Abror",
    "familiya": "Ismatov",
    "tel": 995684342,
    "yosh": 15,
}

print(id(dict))
print(dict, type(dict))

set = {1, 2, 3} #bu set varibel i o'zgaruvchi ichiga bir xil raqm yozib bo'lmedi
set.add(4)
print(set)

integer = 18
floating = 4.5
complex = integer + floating + 4j

print(type(integer))
print(type(floating))
print(type(complex))

p = 1
p -= 2

print(p)

svetY = "yashil"
svetQ = "qizil"
svetS = "sariq"

rang = input("rang tanla (yashil, sariq, qizil): ").lower()

if rang == "yashil" :
    print("yur.")
elif rang == "sariq" :
    print("sabir qil.")
elif rang == "qizil" :
    print("to'xta")
else:
    print("faqat berilgan rangni tanla!")

