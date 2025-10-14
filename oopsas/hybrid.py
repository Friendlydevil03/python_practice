class Character:
    def __init__(self,name,hp,stamina,gender):
        self.name = name
        self.hp = hp
        self.stamina = stamina
        self.gender = gender

    def details_of_char(self):
        print(f"the character name is {self.name}")
        print(f"the character hp is {self.hp}")
        print(f"the character stamina is {self.stamina}")

class Mage(Character):
    def __init__(self,name,hp,stamina,gender,magic,spells):
        super().__init__(name,hp,stamina,gender)
        self.magic = magic
        self.spells = spells

    def details_of_mage(self):
        Character.details_of_char(self)
        print(f"the spell name is {self.spells}")
        print(f"the magic is {self.magic}")

class Swordsman(Character):
    def __init__(self,name,hp,stamina,gender,sword,shield):
        Character.__init__(self,name,hp,stamina,gender)
        self.shield = shield
        self.sword = sword

    def details_of_swordman(self):
        Character.details_of_char(self)
        print(f"has sword {self.sword}")
        print(f"has shield {self.shield}")

class Battlemage(Swordsman,Mage):
    def __init__(self, name, hp, stamina, gender, magic, spells, sword, shield, potions, heal):
        Mage.__init__(self,name,hp,stamina,gender,magic,spells)
        Swordsman.__init__(self, name, hp, stamina, gender, sword, shield)
        self.potions = potions
        self.heal = heal

    def details_of_battlemage(self):
        Character.details_of_char(self)
        Swordsman.details_of_swordman(self)
        print(f"has potions {self.potions}")
        print(f"has heal {self.heal}")


all = Battlemage("hela",2000,1000,"female","divine depature","illuminate",True,True,True,True)
all.details_of_battlemage()



