#Konstruktor, destruktor
#Vorisdorlik, polimorfizim

class Texnika:

    def __init__(self, brend, model, tur):
        self.brend = brend
        self.model = model
        self.tur = tur

    def info(self):
        print("brendi: ",self.brend)
        print("modeli: ",self.model)
        print("turi: ",self.tur)

class Notebooks(Texnika):

    def __init__(self, brend, model, tur, video_card, ram, display):

        super().__init__(brend, model, tur)

        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(self.brend)
        print(self.model)
        print(self.tur)
        print(self.video_card)
        print(self.ram)
        print(self.display)


t = Texnika("Lenovo", "IdeapadGaming", "Gaming")
t.info()

n = Notebooks("Lenovo", "IdeapadGaming", "Gaming", "RTX 3060", "32gb", "4K")
n.more_info()



