class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

class Franchise:
    def __init__(self,address, menus):
        self.adress = address
        self.menus = menus

    def __repr__(self):
        return self.adress

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name                                         #self.name = name ==>object.attribute = passed name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + ' menu available from ' + str(self.start_time) + ' - ' + str(self.end_time)
        #return "{} menu available from {} - {}".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill



# Brunch Menu
# https://docs.python.org/3/library/datetime.html#time-objects
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                    'espresso': 3.00, 'tea': 1.00,'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print(brunch_menu.name)
#print(brunch_menu.items)
#print(brunch_menu.start_time)
#print(brunch_menu.end_time)

# Early Bird Menu
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                    'coffee': 1.50, 'espresso': 3.00}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)
#print(early_bird_menu.name)
#print(early_bird_menu.items)
#print(early_bird_menu.start_time)
#print(early_bird_menu.end_time)

# Dinner Menu
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)
#print(dinner_menu.name)
#print(dinner_menu.items)
#print(dinner_menu.start_time)
#print(dinner_menu.end_time)

# Kids Menu
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu = Menu('Kids', kids_items, 1100, 2100)
#print(kids_menu.name)
#print(kids_menu.items)
#print(kids_menu.start_time)
#print(kids_menu.end_time)

#print(brunch_menu) # def __init__(self): satırını yazmazsak, main.object çıktısını alırız.
#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
#print(Menu('Early Bird', early_bird_items, 1500, 1800).calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
#    ^                                               ^ ==> bu kısmı yukarıda early_bird_menu diye değişkene atayarak kolaylık sağladık.

# menus diye bir liste oluşturduk
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu] # menus yerine menuler de olabilirdi, classın icindeki menus kısmına
#                                                                  parametre olarak menus ya da menuler kısmı geliyor.
#print(menus) # listedeki her bir menünün, örnek olarak, Menu('Early Bird', early_bird_items, 1500, 1800) clasının nesnesideki repr kodu calısıyor.

# 2 tane franchise oluşturduk
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
#print(flagship_store) # aynı şekilde burda da repr kodunda olan self.adress calısıyor.
#print(flagship_store.available_menus(1200))
#print(flagship_store.available_menus(2000))
#print(flagship_store.available_menus(1700))

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Arepa

arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepa = Business("Take a’ Arepa", [arepas_place])

print(arepa.franchises[0])
print(arepa.franchises[0].menus[0])