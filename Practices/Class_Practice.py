# Class OOP
import threading
from plistlib import loads


class Info:
    def __init__(self, name, salry):
        self.name = name,
        self.salry = salry

    def display_info(self, name, salry):
        return f"Xodim: {name}, maoshi: {salry}"

class Treader(Info):
    def display_info(self):
        return f"Treader: {self.name}, maoshi: {self.salry}"

class Developer(Info):
    def display_info(self):
        return f"Developer: {self.name}, maoshi: {self.salry}"

employ1 = Treader("Abrorjon", f"{1000000000000}$")
employ2 = Developer("Asilbek", f"{1000000000000}$")

# print(employ1.display_info())
# print(employ2.display_info())

def function():
    return str('Mo\'nisa') is not str('Asilbek')
# print(function())

#with operatori
lock = threading.Lock()

# with lock:
    # print('Resursga kirish')

with open("telegram.txt", "r") as file:
    content = file.read()
    # print(content)

class Love_obj:
    def __init__(self, name, age, love):
        self.name = name,
        self.age = age,
        self.love = love

    def func_info(self):
        return f"Ismim: {self.name}, yoshim: {self.age}, {self.love} sizni sevaman"

class Asilbek(Love_obj):
    def func_info(self):
        return f"Ismim {self.name}, yoshim: {self.age}, {self.love} sizni sevaman"

class Munisa(Love_obj):
    def func_info(self):
        return f"ismim: {self.name}, yoshim; {self.age}, {self.love} sizni sevaman"

he = Asilbek("Asilbek", 15, "Munisa")
she = Munisa("Munisa", 15, "Asilbek")

# print(he.func_info())
# print(she.func_info())

#Json va pyhton obj

import json

json_data = '{"name": "Ali", "age": 15, "email": "employ@gmail.com"}'

json_to_obj = json.loads(json_data)

print(f"agar tpye dict bo'lsa znachit json ma'lumot turi 100% pythondagi haqiqiy object ga aylanadi {type(json_to_obj)}")
print(f"name: {json_to_obj["name"]}")
print(f"age: {json_to_obj["age"]}")
print(f"email: {json_to_obj["email"]}")
print(f"bu dictionary: {json_to_obj}")

with open("data_json_1", "r") as file:
    file_content = file.read()
    json_data_file = json.dumps(file_content)

if isinstance(json_data_file, dict):
    for key, value in  json_data_file.items():
        print(f"{key}: {value}")
elif isinstance(json_data_file, list):
    for item in json_data_file:
        print(item)
else:
    print("json file da xatolik bor")


print(json_data_file)


