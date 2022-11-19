## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet

## 1-Types
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))

## 2-Class #https://www.python.org/dev/peps/pep-0008/#class-names
#
class Facade:
  pass

## 3-Instantiation #örnekleme

class Facade:
    pass
facade_1 = Facade()

## 4-Object-Oriented Programming
#burda __main__, şuanda çalıştığımız dosya anlamına gelir.
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

## 5-Class Variables
#
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"

class Grade:
    minimum_passing = 65

## 6-Methods
# Method bir fonksiyondur. İlk argümanı her zaman methodu çağırmaktır. fonksiyon gibi düşünebiliriz. self kullanmak önerilir.
# classlarda fonksiyon ==> method
# classlarda fonksiyon parametresi ==> argüman
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

## 7-Methods with Arguments

class Circle:
  pi = 3.14
  def area(self,radius):
    return self.pi*radius**2
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)

print("KODUN DAHA KISA HALİ, GEREKSİZ YERE DEĞİŞKEN ATAYIP KULLANMAYA GEREK YOK")

pizza_area = Circle().area(12/2)
teaching_table_area = Circle().area(36/2)
round_room_area = Circle().area(11460/2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)

## 8-Constructors
# diğer dillerde genelde buna constructor adı verilir, ancak pythonda contructordan bahsediyorsak, __init__ kullanılır genelde.
# iki tarafta da çift alt çizgi dunder method diye geçiyor.
class Circle:
    pi = 3.14
    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: {}".format(diameter))

teaching_table = Circle(36)


class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(diameter=diameter))

teaching_table = Circle(36)

# bir kaç örnek
class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"

class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

## 9-Instance Variables
# sınıflar veri türü için bir şemadır.
# nesneler sınıfların bir örneğidir.
# instance variables, nesnelere özgü değişkenlerdir, sınıf içerisinde değerlendirilmez. sadece bağlı olduğu nesnede değerlendirilir.
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

print(alternative_rocks.store_name)
print(isabelles_ices.store_name)

## 10-Attribute Functions
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))

class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"

hasattr(attributeless, "fake_attribute") # bu sadece olup olmadıgını kontrol eder.
# returns False

getattr(attributeless, "other_fake_attribute", 800) #other_fake_attribte 'a bakıyor yoksa 800 değerini veriyor.
# returns 800, the default value

## 11-Self
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:

        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

## 12-Everything is an Object

dir(5)
print(dir(5))

def this_function_is_an_object(a):
  return a

print(dir(this_function_is_an_object))

## 13-String Representation
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

## 14-Review
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

print(pieter.add_grade(Grade(100)))






