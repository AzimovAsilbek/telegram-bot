# fayillar bilan ishlash
import os
import json

#open, read methodi, read line method, read lines method, read modi.
matn = open("matn.txt", "r")

print(matn.read())

#readline faqat qatorni chiqaradi

matn2 = open("matn.txt", "r")

print(matn2.readline())

#readlines jadval ko'rinishida chiqaradi
matn3 = open("matn.txt", "r")

print(matn3.readlines())

#with, append modi, write modi.

with open("matn.txt", "a") as matn_fayli:
    matn_fayli.write("\nSalom bu append modi")

with open("new_matn.txt", "a") as new_matn_fayl:
    new_matn_fayl.write("\nSalom bu yangi matn fayli")

#write modi
with open("new_file2.txt", "w") as new_file:
    new_file.write("\nBu write modi")
    new_file.write("\nbu yangi qator")

if os.path.exists("new_file2.txt"):
    print("bu fayl mavjud")
else:
    print("\nbu fayl mavjud emas")

#python da Json bilan ishlash
#Jsoni Python objectiga aylantirish

json_data_dict = '{"ismi": "Mo\'nisa", "yoshi": 15, "kasbi": "dasturchi"}'

python_data = json.loads(json_data_dict)
print(python_data)

js_data2 = {
    "ismi": "Asilbek",
    "yoshi": 15,
    "kasbi": "dasturchi"
}

py_to_json = json.dumps(js_data2)
print(py_to_json)

#Json faylni o'qish

with open("py_data.json", "r") as js_file:
    data_json_forReading = json.load(js_file)
    print(data_json_forReading)

#Json ma'lumotini faylga yozish

js_data2 = {
    "ismi": "Asilbek",
    "yoshi": 15,
    "kasbi": "dasturchi"
}

with open("new_senior_programer", "w") as JSdata_file:
    json.dump(js_data2, JSdata_file)