#Ali bobo va 40 qaroqchi o'yini
from math import trunc

#hudut 6 X 6

hudut = [
['*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*']
]

#hudut ni cmd oynasida print qilamiz buning uchun def funcsiyasi va for sikli kere akuratni qilish kere

def print_hudut():
    print("\no'yin hududi\n")
    for i in hudut:
        print(i)

print_hudut()

# Playerni yaratamiz class dan foydalanib birinchi objectni yaratib olib pastdan uni ishlatish uchun fucsiya yozamiz

class Player:
    def __init__(self, x, y, health,):
        self.health = health
        self.x = x
        self.y = y

    def go(self, xP, yP):
        hudut[self.x][self.y] = '*'
        new_x = self.x + xP
        new_y = self.y + yP
        if 0 <= new_x < len(hudut[0]) and 0 <= new_y < len(hudut[0]):
            hudut[self.x][self.y]
            self.x = new_x
            self.y = new_y
        hudut[self.x][self.y] = 'P'

Player1 = Player(0,0,100)

hudut[Player1.y][Player1.x] = 'P'
print_hudut()

while True:
    x = int(input("o'yinchi o'nga 1, yoki chapga -1, o'rnida qolish 0: "))
    y = int(input("o'yinchi tepaga -1, pasga 1, o'rnida qolish 0: "))
    Player1.go(y,x)
    print_hudut()