'''
Есть класс Weapon, который представляет оружие. Он содержит базовые атрибуты, такие как name и damage, 
а также список modifications для хранения различных модификаций оружия.
Метод add_modification позволяет добавлять модификации к оружию.
Метод describe выводит информацию об оружии.
Метод clone использует функцию deepcopy из модуля copy для создания полной копии объекта оружия, 
включая все его атрибуты и модификации.


'''


from copy import deepcopy

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.modifications = []

    def add_modification(self, mod):
        self.modifications.append(mod)

    def describe(self):
        mods = ', '.join(self.modifications)
        return f"{self.name} (Damage: {self.damage}, Modifications: {mods})"

    def clone(self):
        # Use the deepcopy method to create a clone of the weapon
        return deepcopy(self)

def main():
    # Initial Sword Creation and Description
    sword = Weapon("Sword", 50)
    sword.add_modification("Sharpness")
    sword.add_modification("Fire Aspect")
    sword_description = sword.describe()

    # Cloning Sword and Adding Modification
    cloned_sword = sword.clone()
    cloned_sword.add_modification("Unbreaking")
    cloned_sword_description = cloned_sword.describe()
    
    # Example with another weapon
    bow = Weapon("Bow", 30)
    bow.add_modification("Power")
    bow.add_modification("Punch")
    bow_description = bow.describe()

    cloned_bow = bow.clone()
    cloned_bow.add_modification("Infinity")
    cloned_bow_description = cloned_bow.describe()

    return sword_description, cloned_sword_description, bow_description, cloned_bow_description

# Execute the main function and get the results
results = main()
results
