## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-loops/cheatsheet

## 1-Introduction
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)
## 2-Create a For Loop
# for <temporary variable> in <list variable>:
#     <action>
for i in dog_breeds:
    print(i)
for dog in dog_breeds:
    print(dog)
## 3-Using Range in Loops
# range(5) = 0,1,2,3,4 => dolayısıyla toplam rakam 5
promise = "I will not chew gum in class"
for i in range(5):
  print(promise)
## 4-Infinite Loops
# Sonsuz döngülere dikkat.
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  #students_period_A.append(student)
  students_period_B.append(student)  # B yerine A yazılı olsaydı, sonsuz döngü.
  print(student)
## 5-Break
# Döngüdeki şart tamamlandığında, döngüden çıkılır, döngünün her elemanı tamamlanmaz.
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
## 6-Continue
# Listedeki bazı değerleri atlamak için kullanılabilir.
# 21den büyük sayıları yazdırmak için,
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for i in ages:
  if i<21:
    continue #küçük olduğu sürece devam edecek, herhangi bir işlem yapmayacak.
  print(i)   #büyük ise sayıyı output olarak yazıcak.
## 7-While Loops
# Döngü şart sağlanana kadar devam eder.
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    print(len(students_in_poetry))
    student = all_students.pop()  #append sona 1 eleman eklerken, pop sondan 1 eleman çıkarıyor.
    students_in_poetry.append(student)

print(students_in_poetry)
## 8-Nested Loops
# İç içe döngüler.
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)
## 9-List Comprehensions
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)

usernames1 = [word for word in words if word[0] == '@'] # aynı işlevi görüyor.

print(usernames)
print(usernames1)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = []
can_ride_coaster = [i for i in heights if i>161]
print(can_ride_coaster)

## 10-More List Comprehensions
my_upvotes = [192, 34, 22, 175, 75, 101, 97]
# Her bir sayıya 100 eklemek için,
updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]
print(updated_upvotes)

celsius = [0, 10, 15, 32, -5, 27, 3]
# celsius'u fahreneit'e çevirmek için,
fahrenheit = [i*(9/5) + 32 for i in celsius]

print(fahrenheit)
## 11-Review
single_digits = range(10)
squares = []
cubes = []
for i in single_digits:
  squares.append(i**2)
  cubes.append(i**3)
print(squares)
print(cubes)

############################################## CODE CHALLENGES ########################################################
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# Write your function here
def odd_indices(lst):
    new_list = []
    for i in range(1, len(lst), 2):
        new_list.append(lst[i])
    return new_list


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


# Write your function here
def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


# Write your function here
def exponents(bases, powers):
    new_list = []
    for i in range(len(bases)):
        for k in range(len(powers)):
            new_list.append(bases[i] ** powers[k])
    return new_list


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


# Write your function here
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))


# Write your function here
def larger_sum(lst1, lst2):
    sum_lst1 = 0
    for i in lst1:
        sum_lst1 += i
    # return sum_lst1

    sum_lst2 = 0
    for k in lst2:
        sum_lst2 += k
    # return sum_lst2

    if sum_lst1 >= sum_lst2:
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#Write your function here
def same_values(lst1,lst2):
  new_list = []
  for i in range(len(lst1)):
    if lst1[i]==lst2[i]:
      new_list.append(i)
  return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

def same_values(lst1,lst2):

  for i in range(len(lst1)):
    if lst1[i]==lst2[i]:
      return True
  return False

