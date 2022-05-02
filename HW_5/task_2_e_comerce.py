class User:
    def __init__(self, name, mail, adress, password):
        self.name = name
        self.mail = mail
        self.adress = adress
        self.password = password

    def get_username(self):
        return self.mail

    def get_password(self):
        return self.password

    def get_name(self):
        return self.name

    def user_login(self,  check_user_name, check_password):
        assert check_user_name == User.get_username(self), "Wrong user"
        assert check_password == User.get_password(self),  "Wrong pass"
        print(f"Welcome {User.get_name(self)} to our lovely site !")


class Item:
    item_1 = {'name_item1': "Item1", 'quantity_item1': 1, 'price_item1': 10}
    item_2 = {'name_item2': "Item2", 'quantity_item2': 2, 'price_item2': 20}
    item_3 = {'name_item3': "Item3", 'quantity_item3': 3, 'price_item3': 30}
    item_4 = {'name_item4': "Item4", 'quantity_item4': 4, 'price_item4': 40}

    all_items = {**item_1, **item_2, **item_3, **item_4}

    @staticmethod
    def get_available_items():
        return print(Item.all_items)


class Cart:
    def __init__(self, user, item):
        if User.user_login:
            try:
                print(f"Ordered! Your order {item} is confirmed")
            except:
                print("Please Login!")


# new_user = User("Peshkata", "Nqkav_mail", "Pleven", '123')
# new_user.user_login("Nqkav_mail", '123')
# items = Item.get_available_items()
#
# new_order = Cart(new_user, Item.item_1)
# new_order2 = Cart(new_user, Item.item_2)
#

my_user = User("Bate_Cveti", "zemi_toz_mail@be.com", "BG", password=1234)
my_user.user_login(check_user_name="zemi_toz_mail@be.com", check_password=1234)
all_available_items = Item.get_available_items()
i_want = Cart(my_user, Item.item_2)
me_want = Cart(my_user, Item.item_3)



