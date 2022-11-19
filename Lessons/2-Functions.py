#https://www.codecademy.com/learn/paths/computer-science/tracks/cspath-intro/modules/cspath-python-functions/cheatsheet

## 3-Write a Function
# Fonksiyonlar çağırdığımızda içerisine yazılan kodlar çalıştırılır, kod yazılan kısım girintili olmalıdır.
def loading_screen():
    print("This page is loading...")
loading_screen()
## 5-Parameters
# Parantez içerisine yazılanlar fonksiyon'da değişkenlerde kullanabileceğimiz parametrelerdir.
def mult_two_add_three(number):
    print(number * 2 + 3)
mult_two_add_three(0)
def greet_customer(special_item):
    print("Welcome to Engrossing Grocers.")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
greet_customer("peanut butter")
## 6-Multiple Parameters
# Birden fazla değişken
def mult_x_add_y(number, x, y):
    print(number * x + y)
mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)
def greet_customer(grocery_store, special_item):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
greet_customer("Stu's Staples", "papayas")
## 7-Keyword Arguments
# Fonksiyon yazarken, içerisindeki parametrelerin bazıları sabit olmasını isteriz, parantez içerisinde = ile sabitleyebiliriz.
# Sabit olacak olan değer fonksiyonda en sona gelmelidir.
def greet_customer(special_item, grocery_store="Engrossing Grocers"):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
greet_customer("bananas")
def create_spreadsheet(title, row_count=10):
    print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows.")
create_spreadsheet("Downloads") #Default olan 10 burda çalışır, ancak aşağıda parametre olarak 9 yazdığımız için 9 çalışır, sabit 10'u görmez.
create_spreadsheet("Applications", 9)
## 8-Return
# Return işlevi, fonksiyon içerisinde yazılan değeri tutmaya yarar.
# Eğer return kullanmazsak, değer hesaplanır ve içinde kalır, output almak istersek değer none olarak gözükür.
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calculate_age(2020, 1995)
print("I am " + str(my_age) + " years old.")
## 9-Multiple Return
# Fonksiyon içerisinde birden fazla fonksiyon içindeki değişkenin değerini tutmaya yarar. Daha sonra bunları değişkene atayabiliriz.
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit
low, high = get_boundaries(100, 20)
print("Low limit: "+str(low)+", high limit: "+str(high))
def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)
## 10-Scope
# Fonksiyon içerisie yazılan değişkenler, fonksiyon içerisinde kalır, dışarıda çağırdığımızda gelmez, çünkü öyle bir değişken tanımlanmamıştır.
# Ancak değişkeni fonksiyon dışında yazıp, fonksiyon içerisinde kullanılabilir.
current_year=2048
def calculate_age(birth_year):
  age = current_year - birth_year
  return age
print(current_year)
print(calculate_age(1970))
# 11-Review
def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)
print(song)