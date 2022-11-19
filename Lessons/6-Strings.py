## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-strings/cheatsheet

## 2-They're all Lists!
# Stringler de bir listedir, dolayısıyla stringlerdeki harfler de indexlenmiştir.
my_name = "Hamdi"
first_initial = my_name[0]
## 3-Cut Me a Slice of String
favorite_fruit = "Blueberry"
favorite_fruit[:4] #'blue'
favorite_fruit[4:] #'berry'
## 4-Concatenating Strings
fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name,last_name):
  account_name=first_name[:3]+last_name[:3]
  return account_name
new_account = account_generator(first_name,last_name)
print(new_account)
## 5-More and More String Slicing
# len komutu ile stringin uzunluğunu bulabiliriz, boşluklar dahil.
favorite_fruit = "blueberry"
len(favorite_fruit) #9
fruit_sentence = "I love blueberries"
len(fruit_sentence) #18
length = len(favorite_fruit)
#favorite_fruit[length] #hata verecektir, çünkü 9 yazıldığı için 10.elemanı arayacak, öyle bir eleman olmadığı için hata verir.
favorite_fruit[length-1]
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name,last_name):
  return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
temp_password = password_generator(first_name,last_name)

## 6-Negative Indices
# Sondan x kadar eleman için -x yazılabilir
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]
## 7-String are Immutable
# Stringslerin içeriği değiştirilemez.
first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R"
fixed_first_name = "R" + first_name[1:]
## 8-Escape Characters
#favorite_fruit_conversation = "He said, "blueberries are my favorite!""
#favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""  ???
## 9-Iterating through Strings
def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter
print(get_length("ankara"))
## 10-Strings and Conditionals (Part One)
def letter_check(word,letter):
  for i in word:
    if i == letter:
      return True
  return False
  #bu return truelerde girintiyi ve mantıgı cozemedım

print(letter_check("strawberry", "a"))
print(letter_check("strawberry", "o"))

## 11-Strings and Conditionals (Part Two)
def contains(big_string,little_string):
  if little_string in big_string:
    return True
  return False

print(contains("watermelon","melon"))
print(contains("watermelon","berry"))

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
print(common_letters("banana", "cream"))
## 12- Review
def username_generator(first_name, last_name):
  if len(first_name) < 3 :
    username = first_name + last_name[:4]
  elif len(last_name) < 4 :
    username = first_name[:3] + last_name
  elif len(first_name) < 3 and len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username
print(username_generator("Abe", "Simpson"))

def password_generator(username):
  password = username[-1] + username[:len(username)-1]
  return password
print(password_generator(username_generator("Abe", "Simpson")))
#alternatif çözüm
def password_generator(user_name):
  password = ""
  for i in range(0, len(user_name)):
    password += user_name[i - 1]
  return password

## 2.2-Formatting Methods
#.title() = baş harfleri büyük yapıyor
#.lower() = bütün harfleri küçük
#.upper() = bütün harfleri büyük
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)
## 2.3-Splitting Strings I
# Stringsteki cümleleri ayırmaya yarar.
line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words)

## 2.4-Splitting Strings II
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')  #virgüllerden ayırarak liste oluşturuyor. eğer sonra virgül olsaydı "" diye bir eleman daha oluşacaktı.
print(author_names)
print(author_names[0:1])  ## tek stringli liste

"""for i in author_names:
  print(author_names[i])""" #burda i, author_names'deki değerlere bakıp string olarak algılıyor, dolayısıyla indeks olarak çalışmıyor.

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)
# alternatif
last_names_from_seperated_names = []
for names in author_names:
  seperated_names = names.split()
  print(seperated_names)
  last_names_from_seperated_names.append(seperated_names[-1])
  print(last_names_from_seperated_names)
## 2.5-Splitting Strings III
#anlamadım valla
#\n Newline
#\t Horizontal Tab
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
for i in spring_storm_lines:
  print(i)

## 2.6-Joining Strings I
# başa " " koymak önemli yoksa boşluksuz yazar.
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

## 2.7-Joining Strings II
# " " arasına ne yazarsak onla bağlar.
# Satır başı için "\n".join gibi, tersi düşün
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

## 2.8-.strip()
# istenmeyen boşlukları karakterleri silmeye yarar
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped  = []
for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())

print(love_maybe_lines_stripped)

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

## 2.9-Replace
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer","Toomer")

## 2.10-Find
# aranan ifadenin string deki indeksini verir.
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

## 2.11-Format
# Stringlerde yazarken çok fazla karışıklık olmasın diye, değişkenleri sonda göstermeye yarar.
# Önceden + işareti ile ekliyorduk.
# Şimdi tek seferde yazıp değişkenin geleceği yere {} eklereyek, en sona .format() ile yapıyoruz.
# \ karakterlere dikkat.
def poem_title_card(poet, title):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc

def poem_title_card(poet, title):
  return """The poem "{}" is written by {}.""".format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

## 2.12-Format II
# Küme parantezlerinin içerisine değişkenin adı yazılabilir, format içerisinde de eşleştirilerek sırası önemsiz hale getirilebilir.
# Ancak fonksiyonu yazarken sıralama önemlidir.

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

## 2.13-Review
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems) #Tek bir string halinde olan veriyi yazdırdık.
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list) #Bu string'i virgüllerden bölerek verilerimizi oluşturduk.

highlighted_poems_stripped = []
for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())
print(highlighted_poems_stripped) #tek tek verilerin içerisine girip strip yaparak boşlukları kestik.

highlighted_poems_details = []
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(':'))
  print(highlighted_poems_details) #veri setleri içerisinde : : olanlardan kesereki içinde diğer verileri oluşturduk
titles = []
poets = []
dates = []
for i in highlighted_poems_details:
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])
# print(titles)
# print(poets)
# print(dates)
for i in range(len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))

#############################################       CODE CHALLENGES        ############################################
## 2-Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  count = 0
  for i in range(len(letters) - 1):
    if letters[i] in word:
      count += 1
  return count
"""def unique_english_letters_(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques"""

a = input("Say one word")
print(unique_english_letters(a))

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

## 3-Count X
# Write your count_char_x function here:
def count_char_x(word,x):
  number_of_times_x = 0
  for i in range(len(word)): # range(11) = [0,1,2,3,4,5,6,7,8,9,10] olduğu için sorun olmuyor. word[11] olsa hatar verirdi zaten.
    if word[i] == x:
      number_of_times_x +=1
  return number_of_times_x

"""def count_char_x(word, x):
  occurrences = 0
  for letter in word:
    if letter == x:
      occurrences += 1
  return occurrences"""

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
print(count_char_x("mississippi", "i"))
# should print 4

## 4-Count Multi X
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

# Uncomment these function calls to test your  function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

word = "missippi" #iss oldugunda boşluk yanyana ississ olursa "" koyuyor ??
x = "iss"
word_new = word.split(x)
print((word_new))
print(len(word_new))
print(len(word_new)-1)

## 5-Substring Between
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word

# Uncomment these function calls to test your tip function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

## 6-X Length
# Write your x_length_words function here:
def x_length_words(sentence, x):
  splitted_sentence = sentence.split(" ")
  for i in splitted_sentence:
    if len(i) < x:
      return False
  return True #Her biri için nasıl bakıyor ki, bir de bu bir girintili daha yazılsa fark ne olur.

# Uncomment these function calls to test your  function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

## 7-Check Name
# Write your check_for_name function here:
def check_for_name(sentence,name):
  lower_sentence = sentence.lower()
  lower_name = name.lower()
  splitted_sentence=lower_sentence.split()
  if splitted_sentence[-1] != lower_name:
    return False
  return True

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

## 8-Every Other Lether
# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

# Uncomment these function calls to test your tip function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

## 9-Reverse
# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  for i in range(len(word)):
    reverse += word[-i-1]
  return reverse
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

## 10-Make Spoonerism
# Write your make_spoonerism function here:
def make_spoonerism(word1,word2):
  return word1.replace(word1[0],word2[0])+ " " +word2.replace(word2[0],word1[0])

"""def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]"""

# Uncomment these function calls to test your tip function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

## 11-Add Exclamation
# Write your add_exclamation function here:
def add_exclamation(word):
  if len(word) < 20:
    for i in range(20- len(word)):
      word += "!"
  return word

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn