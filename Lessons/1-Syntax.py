#https://www.codecademy.com/learn/paths/computer-science/tracks/cspath-intro/modules/cspath-python-syntax/cheatsheet

## 1-Welcome
my_name = "Hamdi"
print("Hello and Welcome" + my_name + "!")
## 2-Comments
# yorum yapmaya yardımcı
## 4-Strings
print('Hamdi')
print("Hamdi")
## 5-Variables
# değişken atamak = ile yapılıyor.
meal = "An english muffin"
## 6-Errors
# SynxtaxError -> Noktalama yanlışlıkları, komut hatası veya eksik parantez gibi hatalardan kaynaklanır.
# NameError -> Atanmamış değişken varsa bu yüzden kaynaklanır.
## 7-Numbers
# İki tip sayı vardır. int, tamsayı; float, kesirli sayı
an_int = 2
a_float = 2.1
## 8-Calculations
print(25*68+13/28)
## 10-Exponents
# Üslü sayıları ifade ederken ** işareti kullanılır.
print(6**2) #  6 üzeri 2
# 11-Modulo
# Bölme işleminden kalanı bulmak için % işareti kullanılır.
my_team= 27 % 4
print(my_team)
# 12-Concatenation = Birleştirme, hem sayılar için hem de yazılar için kullanılabilir.
string1="Hello"
string2="World!"
string1_2=string1+string2
print(string1_2)
birthday_string = "I am "
age = 25
birthday_string_2 = " years old today!"
full_birthday_string = birthday_string + str(age) + birthday_string_2
print(full_birthday_string)
print(birthday_string, age, birthday_string_2)
# 13-Plus Equals
# += işareti ile değişkenlerimizi üstüne toplayarak güncelleyebiliriz.
total_price = 0
new_sneakers = 50.00
total_price += new_sneakers
# 14-Multi-Line Strings
# """ bla bla """ veya ''' bla bla ''' şeklinde string yazabiliriz.
# 16-Input
favorite_flightless_bird = input("What is your favorite flightless bird?")
print(favorite_flightless_bird)

