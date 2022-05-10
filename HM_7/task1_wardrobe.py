class Wardrobe:
    def __init__(self, capable_size_of_wardrobe, color):
        self.capable_size_of_wardrobe = capable_size_of_wardrobe
        self.color = color

    def __repr__(self):
        return f"Your Wardrobe has color '{self.color}' and and can collect" \
               f" only '{self.capable_size_of_wardrobe}' items "


my_wordrobe = Wardrobe(5, "white")
print(my_wordrobe)


class Clothing:
    is_collected = False
    all_available_items = 0

    def __init__(self, type_of_clothing, color, make):
        self.type_of_clothing = type_of_clothing
        self.color = color
        self.make = make
        Clothing.all_available_items +=1

    def __repr__(self):
        return f"Your lovely '{self.type_of_clothing}' that is color '{self.color}' and made by '{self.make}'"

    @classmethod
    def collect_them_all(cls):
        cls.is_collected = True

    @staticmethod
    def free_slot():
        if Clothing.all_available_items > my_wordrobe.capable_size_of_wardrobe and Clothing.is_collected == False:
            print(f"No space in your wordrobe. Cant get all '{Clothing.all_available_items}' items in it")
            exit()
        elif Clothing.is_collected:
            return my_wordrobe.capable_size_of_wardrobe - Clothing.all_available_items

        else:
            return Clothing.all_available_items


chorapi = Clothing(type_of_clothing="Chorapi", color="Black", make="Moite_chorapi_made")
riza = Clothing(type_of_clothing="Riza", color="White", make="Diamant")
pantalon = Clothing(type_of_clothing="Pantalon", color="Blue", make="Levi`s")
teniska = Clothing(type_of_clothing="Teniska", color="Brown", make="Nike")
fanela = Clothing(type_of_clothing="Fanela", color="Purple", make="Reebok")
#nqma_mqsto = Clothing(type_of_clothing="Potnik", color="White", make="Moq_potnik")


print(f"""
Is your {chorapi} in the Wardrobe ? {Clothing.is_collected}
Is your {riza} in the Wardrobe ? {Clothing.is_collected}
Is your {pantalon} in the Wardrobe ? {Clothing.is_collected}
Is your {teniska} in the Wardrobe ? {Clothing.is_collected}\n
You have {Clothing.free_slot()} slots left for more clothing
""")
chorapi.collect_them_all()
print(f"""MAGIC :) \ncheck your Wardrobe again
Is your {chorapi} in the Wardrobe ? {Clothing.is_collected}
Is your {riza} in the Wardrobe ? {Clothing.is_collected}
Is your {pantalon} in the Wardrobe ? {Clothing.is_collected}
Is your {teniska} in the Wardrobe ? {Clothing.is_collected}\n
You have {Clothing.free_slot()} slots left for more clothing
""")



