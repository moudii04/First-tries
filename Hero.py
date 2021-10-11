champs = ["Tank", "Mage", "Assassin ", "Suppport"]
champs_def = ["Un guerrier qui n'a pas peur de foncer dans le tas",
              "Un sorcier qui fait appelle a la magie",
              "Un expert en furtivité et maitre des dagues",
              "Un puissant mage qui dédie ses pouvoirs a aider ses alliés"
              ]


class Move:

    # Parce que c'est bien de marcher :3

    def __init__(self):
        self.type = "Un joli bateau"

    def move_forward(self, hero):
        hero.move_forward()

    def move_backward(self, hero):
        hero.move_backward()

    def move_left(self, hero):
        hero.move_left()

    def move_right(self, hero):
        hero.move_right()


class Skill:

    # DES SUPERPOUVOIRS !

    def __init__(self, power=0):
        self.power = power

    def provocation(self, hero):
        hero.provocation()

    def fire_ball(self, hero):
        hero.fire_ball()

    def camouflage(self, hero):
        hero.camouflage()

    def buff_magic(self, support, hero):
        support.buff_magic(hero)


class Hero:

    class Sorcerer:
        pass

        position = [0, 0]

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move_forward(self):
        self.position[1] += 1

    def move_backward(self):
        self.position[1] -= 1

    def move_left(self):
        self.position[0] -= 1

    def move_right(self):
        self.position[0] += 1

    def __repr__(self):
        if self.position == [0, 0]:
            return f"le héros {self.name} est a la position de départ : "\
                f"{self.position}"
        elif self.position != [0, 0]:
            return f"le héros  {self.name} s'est déplacé a {self.position}."


class Tank(Hero):

    def __init__(self, name, position=[0, 0], defense=2, magic=0):
        Hero.__init__(self, name, position)
        self.defense = defense
        self.magic = magic
        print("Invocation de la classe Tank... \nLe héros"
              " {} est invoqué en Tank".format(self.name))

    def provocation(self):
        self.defense += 5
        print(f"la défense est augmenté jusqu'a {self.defense}")

    def fire_ball(self):
        print("{} essaie de lancer une boule de feu ..."
              "\nsauf qu'un tank ca tire pas du feu :3".format(self.name))


class Mage(Hero):

    def __init__(self, name, position=[0, 0], magic=1):
        Hero.__init__(self, name, position)
        self.magic = magic
        print("Le maitre des flammes {} a décidé de rejoindre"
              "l'aventure !".format(self.name))

    def fire_ball(self):
        print("{} essaie de lancer une boule de feu".format(self.name))
        if self.magic > 2:
            print("{} lance une boule de feu de puissance {}.".format(
                self.name, self.magic))
        elif self.magic <= 2:
            print("Pas assez de mana !")


class Support(Hero):

    def __init__(self, name, position=[0, 0], magic=3):
        Hero.__init__(self, name, position)
        self.magic = magic

    def buff_magic(self, hero):
        if hero.magic > 0:
            hero.magic += 5
            print(
                f"{self.name} buff la magie du héros {hero.name}"
                " de 2 ! ")
        else:
            print("Le héros choisi n'est pas un mage ! ")

    def definition():
        print("Les supports sont des héros qui buffent la magie des alliés")


class Assassin(Hero):

    def __init__(self, name, position=[0, 0], magic=0, stealth=5):
        """rerejoero."""
        Hero.__init__(self, name, position)
        self.magic = magic
        self.stealth = stealth
        self.camouflaged = False

    def camouflage(self):
        if not self.camouflaged:
            self.camouflage = True
            print("Je suis invisible ...")
        elif self.camouflage:
            print("Invisibilité prolongée ...")


move = Move()
skill = Skill()


def fun(a):
    return a.capitalize()


print("choisissez votre classe :")

for x, y in zip(champs, champs_def):
    print("{0} : {1}".format(x, y))

try:
    entry = str(input("Your choice : "))
except Exception:
    print("Une erreur est survenu, bizarre")

cap_entry = fun(entry)

if cap_entry in champs:
    print("Choix confirmé")
elif cap_entry not in champs:
    print("Il y'a eu une erreur lors de la selection du choix")
    SystemExit


y = str(input("Choose your name : "))

if cap_entry == "Tank":
    player = Tank(y)
elif cap_entry == "Mage":
    player = Mage(y)
elif cap_entry == "Assassin":
    player = Assassin(y)
elif cap_entry == "Support":
    player = Support(y)

deleted_champs = champs.index(cap_entry)
champs.pop(deleted_champs)
