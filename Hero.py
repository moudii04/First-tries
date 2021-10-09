class Move:
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
    def __init__(self, power):
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

    def __init__(self, name, position=0.0):
        self.name = name
        self.position = position

    def move_forward(self):
        self.position += 0.1

    def move_backward(self):
        self.position -= 0.1

    def move_left(self):
        self.position -= 1.0

    def move_right(self):
        self.position += 1.0

    def __repr__(self):
        return f"le héros {self.name} est a la position {self.position}"


class Tank(Hero):

    def __init__(self, name, position=0.0, defense=2, magic=0):
        self.name = name
        self.position = position
        self.defense = defense
        self.magic = magic

    def provocation(self):
        self.defense += 5
        print(f"la défense est augmenté jusqu'a {self.defense}")


class Mage(Hero):

    def __init__(self, name, position=0.0, magic=1):
        self.name = name
        self.position = position
        self.magic = magic

    def fire_ball(self):
        if self.magic > 2:
            print("Boule de feu !")
        elif self.magic <= 2:
            print("Pas assez de mana !")


class Support(Hero):

    def __init__(self, name, position=0.0, magic=3):
        self.name = name
        self.postion = position
        self.magic = magic

    def buff_magic(self, hero):
        if hero.magic > 0:
            hero.magic += 5
            print(
                f"la magie du héros {hero.name} est devenu {hero.magic} ")
        else:
            print("Le héros choisi n'est pas un mage ! ")


class Assassin(Hero):

    def __init__(self, name, position=0.0, magic=0, stealth=5):
        self.name = name
        self.position = position
        self.magic = magic
        self.stealth = stealth
        self.camouflaged = False

    def camouflage(self):
        if not self.camouflaged:
            self.camouflage = True
            print("Je suis invisible ...")
        elif self.camouflage:
            print("Invisibilité prolongée ...")


zampted = Support("zampted")
moudi = Tank("moudi")
slim = Assassin("slim")
skill = Skill(5)

zampted.buff_magic(moudi)
skill.camouflage(slim)
