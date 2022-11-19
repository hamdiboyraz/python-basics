## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-dictionaries/cheatsheet

## 1-What is a Dictionary?
# Sözlük, bir kümedir.
# {} ile oluşturulur.
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# living room keydir, 21 value dir.
print(sensors)

## 2-Make a Dictionary
# value ler string,integer,list, hatta mix bile olabilir.
translations = {"mountain":"orod", "bread":"bass", "friend":"mellon", "horse":"roch"}

## 3-Invalid Keys
# key değerleri liste olmamalı, string,number gibi değişmeyen ifadeler olmalı, hash value
#children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}  #TypeError: unhashable type, value, key
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]} # key, value

## 4-Empty Dictionary
my_empty_dictionary = {}

## 5-Add a Key
#my_dict["new_key"] = "new_value"
animals_in_zoo ={}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

## 6-Add Multiple Keys
# Birden fazla Key i eklemek için .update() kullanılır, içi aynı kümede olduğu gibi {} formatında yazılır.
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper":138475, "stringQueen":85739})
print(user_ids)

## 7-Overwrite Values
# Var olan bir değeri değiştirmek için, dictionaries'e yeni bir key ekler gibi ekleriz.
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] += " Moonlight" #stringin içine ekledi, ilginç
print(oscar_winners)

## 8-List Comprehensions to Dictionaries
# listelerden oluşan key ve value değerlerini list comprehension yardımıyla sözlük oluşturabiliriz.
# küme ayracı kullanılıyor.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)} #students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)
drinks_to_caffeine = {i:k for i,k in zipped_drinks }
print(drinks_to_caffeine)

## 9-Review
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {i:k for i,k in zip(songs,playcounts)}
print(plays)
plays["Purple Haze"] = 1
plays.update({"Respect":94}) #plays["Respect"] = 94 aynı şey
print(plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)

## 2.2-Get A Key
# Dictionaries ten veri çekme
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

## 2.3-Get an Invalid Key
# Dictionary den olmayan veriyi çekmeye çalıştığımızda KeyError alırız
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

## 2.4-Try/Except to Get A Key

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
#caffeine_level["matcha"] =30
try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

## 2.5-Safely Get a Key
# Hata almaktansa .get() komutu ile verileri çağırabiliriz, eğer yoksa, none outputunu verecektir.
# Veya istediğimiz bir sonucu almak istiyorsak .get(cağırmak istediğimiz değer, buraya istediğimiz cıktıyı yazabiliriz)
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder",100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash")
print(stack_id)
stack_id = user_ids.get("superStackSmash",100000)
print(stack_id)

## 2.6-Delete a Key
# Dictionary deki bir key i silmek istersek .pop() komutunu kullanabiliriz. Eğer o veri yoksa .get() de olduğu gibi, istediğimiz değeri yazdırabiliriz.
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains",0)  # stamina grains i sözlükten siliyor, değeri neysel health_points e ekliyor, eğer sözlükte yoksa 0 ekliyor
health_points += available_items.pop("power stew",0)
health_points += available_items.pop("mystic bread",0)
print(available_items)
print(health_points)

## 2.7-Get All Keys
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
for i in test_scores.keys():
  print(i)
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

## 2.8-Get All Values
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores.values()))
for i in test_scores.values():
  print(i)
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for i in num_exercises.values():
  total_exercises +=i
print(total_exercises)

## 2.9-Get All Items
#(key, value)
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for i,k in pct_women_in_occupation.items():
  print("Women make up {} percent of {}s.".format(k,i))
  print("Women make up " + str(k) + " percent of " + i + "s.")

## 2.10-Review
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key,value in spread.items():
  print("Your {} is the {} card.".format(key,value))

################################################# CODE CHALLENGES #####################################################
## 2-Sum Values
# Write your sum_values function here:
def sum_values(my_dictionary):
  total = 0
  for i in my_dictionary.values():
    total += i
  return total
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

## 3-Even Keys
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total = 0
  for i,k in my_dictionary.items():
    if i % 2 == 0:
      total +=k
  return total
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#Alternatif
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

## 4-Add Ten
# Write your add_ten function here:
def add_ten(my_dictionary):
  for i,k in my_dictionary.items():
    my_dictionary[i] = k+10
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#Alternatif
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

## 5-Values That Are Keys
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  liste = []
  for i in my_dictionary.keys():
    if i in my_dictionary.values():
      liste.append(i)
  return liste

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

##Alternatif
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:  # burası bir değişik geldi, direk my_dictionary içinde arıyor.
      value_keys.append(value)
  return value_keys

## 6-Largest Value
# Write your max_key function here:
def max_key(my_dictionary):
  largest_key =[]
  largest_value = 0
  for i,k in my_dictionary.items():
    if k > largest_value:
      largest_value = k
      largest_key = i
  return largest_key
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

##Alternatif
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

## 7-Word Length Dict
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  dictionary = {}
  for i in words:
    dictionary[i]=len(i)
  return dictionary

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

## 8-Frequency Count
"""def frequency_dictionary(words):
  freqs = {}
  for i in words():
    if i in words:
      freqs[i] += 1

  return freqs"""

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

## 9-Unique Values
# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

## 10-Count First Letter
# Write your count_first_letter function here:
def count_first_letter(names):
  dictionary = {}
  for i in names:
    if i[0] not in dictionary:
      dictionary[i[0]] = 0
    dictionary[i[0]] += len(names[i])

  return dictionary

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

#alternatif
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

## ***
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory) # true false verir.