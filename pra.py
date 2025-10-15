# Base Class
class Character:
    def __init__(self, name, hp, stamina, gender):
        self.name = name
        self.hp = hp
        self.stamina = stamina

        print(f"Gender: {self.gender}")


# Mage Class
class Mage(Character):
    def __init__(self, name, hp, stamina, gender, magic, spells):
        Character.__init__(self,name, hp, stamina, gender)
        self.magic = magic
        self.spells = spells

    def details_of_mage(self):
        super().details_of_char()
        print(f"Magic Type: {self.magic}")
        print(f"Spell: {self.spells}")


# Swordsman Class
class Swordsman(Character):
    def __init__(self, name, hp, stamina, gender, sword, shield):
        Character.__init__(self,name, hp, stamina, gender)
        self.sword = sword
        self.shield = shield

    def details_of_swordsman(self):
        super().details_of_char()
        print(f"Sword: {self.sword}")
        print(f"Shield: {self.shield}")


# Hybrid Class (inherits both Mage + Swordsman)
class BattleMage(Mage, Swordsman):
    def __init__(self, name, hp, stamina, gender, magic, spells, sword, shield, potions, heal):
        # Call Mage constructor first using super()
        Mage.__init__(self, name, hp, stamina, gender, magic, spells)
        # Then initialize Swordsman part
        Swordsman.__init__(self, name, hp, stamina, gender, sword, shield)
        # Extra attributes for BattleMage
        self.potions = potions
        self.heal = heal

    def details_of_battlemage(self):
        print("\n--- BattleMage Details ---")
        self.details_of_char()
        print(f"Magic: {self.magic}")
        print(f"Spell: {self.spells}")
        print(f"Sword: {self.sword}")
        print(f"Shield: {self.shield}")
        print(f"Potions: {self.potions}")
        print(f"Heal Ability: {self.heal}")


# Another derived class combining everything (Hybrid of Hybrid!)
class AccessAll(BattleMage):
    def __init__(self, name, hp, stamina, gender, magic, spells, sword, shield, potions, heal):
        super().__init__(name, hp, stamina, gender, magic, spells, sword, shield, potions, heal)

    def details_of_access_all(self):
        print("\n=== Access All Character ===")
        self.details_of_battlemage()


# Create object
all_char = AccessAll("Hela", 2000, 1000, "Female", "Divine Departure", "Illuminate", "Dragon Blade", "Golden Shield", True, True)

# Display all info
all_char.details_of_access_all()
