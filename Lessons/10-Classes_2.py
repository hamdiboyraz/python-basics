## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet

class Dog(object):                                                        #object
    def __init__(self, name, age):                                        #constructor
        self.name = name                                                  #attribute
        self.age = age                                                    #attribute

    def speak(self):                                                      #method
        print("Hi I am", self.name, 'and I am', self.age, 'years old.')

    def add_weight(self, weight):                                         #method
        self.weight = weight                                              #attribute

class Cat(Dog):                                                           #inheritance
    def __init__(self,name, age, color):
        #super().__init__(name, age)
        self.color = color

tim = Dog('tim', 6)
tim.speak()

## 1-Inheritance
# class yazarken başka classlardan yardım almak

class User:                          #Base Class // Parent Class  // Super Class
  is_admin = False
  def __init__(self, username):
    self.username = username

class Admin(User):                   #Sub Class // Child Class
  is_admin = True

class Bin:
  pass

class RecyclingBin(Bin):
  pass

## 2-Exceptions
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#Pythonda hatalarla karşılaştığımızda, hata vermesi yerine başka bir şey yapmasını isteriz, print veya koddan çıkış gibi
#exception python un built in yani hazır olarak geçiyor
#aşağıdaki kodda bir tane class yazdık, ordaki değer 0 ın altına düştüğünde outofstock a başvurmasını istedik
#outofstock "subclass" ını yazarken de pythonun exception classından yardım aldık.
# Define your exception up here:
class OutOfStock(Exception):
    pass


# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')

## 3-Overriding Methods
#sub classlarda, base classdaki bir argümanın farklı olmasını istiyorsak, overriding methods dan yararlanırız.

class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text                      # User base classı yardımıyla admin sub classı oluşturduk, ancak
                                                     # User base classtan farklı olarak içindeki bir şeyi değiştirdik.

## 4-Super()
#alt sınıfa yeni bir şey eklemek istersek base classın girdilerini de tekrar hatırlatmak icin init kullanılır.

class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40

##5-Interfaces
class Chess:
    def __init__(self):
        pass
    def play(self):
        print("Playing chess!")

class Checkers:
    def __init__(self):
        pass
    def play(self):
        print("Playing checkers!")

def play_game(chess_or_checkers):
  chess_or_checkers.play()

chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()

for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)


class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .00005

## 6-Polymorphism
# + operatörü benzer data tiplerinde kullanılması, Polymorphism  ' a bir örnektir.
# For an int and an int, + returns an int
2 + 4 == 6

# For a float and a float, + returns a float
3.1 + 2.1 == 5.2

# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]


#len() fonksiyonu gibi
# tip farketmeksizin kaç veri oldugunu söylüyor
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))

## 7-Dunder Methods I

class Color:
  def __init__(self, red, blue, green):
    self.red = red
    self.blue = blue
    self.green = green

  def __repr__(self):
    return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)

  def add(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)

red = Color(255, 0, 0)
blue = Color(0, 255, 0)

magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 255, 0)"

class Color:
  def __add__(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)

red = Color(255, 0, 0)
blue = Color(0, 255, 0)
green = Color(0, 0, 255)

# Color with RGB: (255, 255, 0)
magenta = red + blue

# Color with RGB: (0, 255, 255)
cyan = blue + green

# Color with RGB: (255, 0, 255)
yellow = red + green

# Color with RGB: (255, 255, 255)
white = red + blue + green


class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
salt = sodium + chlorine

## Dunder Methods II
#https://docs.python.org/3/library/stdtypes.html#typeiter
class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions

  def __iter__(self):
    return iter(self.user_list)

  def __len__(self):
    return len(self.user_list)

  def __contains__(self, user):
    return user in self.user_list

class User:
  def __init__(self, username):
    self.username = username

diana = User('diana')
frank = User('frank')
jenn = User('jenn')

can_edit = UserGroup([diana, frank], {'can_edit_page': True})
can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})

print(len(can_edit))
# Prints 2

for user in can_edit:
  print(user.username)
# Prints "diana" and "frank"

if frank in can_delete:
  print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")


class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers

    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, i):
        return i in self.lawyers


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

## 9-Review
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()