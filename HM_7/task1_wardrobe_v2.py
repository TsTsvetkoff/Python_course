class Wardrobe:
    def __init__(self):
        self._opened = False
        self.clothes = []

    def __repr__(self):
        return str(self.clothes, self._opened)

    @property
    def _get_open(self):
        return self._opened

    def now_open_it(self):
        self._opened = True

    def now_close_it(self):
        self._opened = False

    def put_clothing_in_wardrobe(self, clothing):
        clothing.in_wadrobe = True
        self.clothes.append(clothing)

    def remove_clothing_fom_wardrobe(self, clothing):
        clothing.in_wadrobe = False
        self.clothes.remove(clothing)

    def clear_your_wardrobe(self):
        for clothing in self.clothes:
            clothing.in_wadrobe = False

        self.clothes.clear()


class Clothingz:
    """
    Here we define different clothing that to interact with the wardrobe created
    """
    def __init__(self, type_clothing, size):
        self.type_clothing = type_clothing
        self.size = size
        self.__clothing_in_wardrobe = False
        self.in_wadrobe =  False

    def __repr__(self):
        return f"Your '{self.type_clothing}' has color '{self.color}' and its size {self.size}"

    def get_type_clothing(self):
        return self.type_clothing

    def set_type_clothing(self, type_clothing):
        self.type_clothing = type_clothing

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    my_kind_of_clothing = property(get_type_clothing, set_type_clothing)
    my_color = property(get_color, set_color)


chorap = Clothingz(type_clothing="чорапи", size="50")
chorap.color = "Кафеви"
print(chorap)
chorap.my_kind_of_clothing = "Дебели чорапи"
print(chorap)

riza = Clothingz(type_clothing="Риза", size="XL")
riza.color = "Бяла"
print(riza)
riza.size = "M"
print(riza)

garderob = Wardrobe()
print(f"Отворен ли е гардероба: {garderob._opened}")
if not garderob._opened:
    garderob.now_open_it()

print(f"A сега отворен ли е гардероба:{garderob._opened}")

garderob.put_clothing_in_wardrobe(chorap)
garderob.put_clothing_in_wardrobe(riza)

print(f"{garderob.clothes} са прибрани прилежно в гардероба. Имаш {len(garderob.clothes)} дрехи в гардероба ")

garderob.remove_clothing_fom_wardrobe(chorap)

print(f"{garderob.clothes} са прибрани прилежно в гардероба. Имаш {len(garderob.clothes)} дрехи в гардероба ")

print(f"Все още ли е отворен гардероба: {garderob._opened}")
if garderob._opened:
    garderob.now_close_it()

print(f"A сега отворен ли е гардероба: {garderob._opened}")
