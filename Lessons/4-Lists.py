# https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-lists/cheatsheet

# 1-What is a list?
# Değişkene birden fazla verileri yüklemeye yarar.
heights = [61, 70, 67, 64]
# 2-Lists II
# Integer ve strings birarada olabilir.
ints_and_strings = [1, 2, 3, 'four', 'five','six']
sam_height=['Sam', 67]
# 3-List of Lists
#Liste içinde veri listeleri olabilir.
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
ages=[['Aaron', 15], ['Dhruti', 16]]
# 4-Zip
# zip komutu ile iki listeyi birbiriyle birleştirebiliriz.
# zip ile bileştirdikten sonra listeyi görmemiz için list() komutunu kullanmalıyız.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]
names_and_heights = zip(names, heights)
print(names_and_heights) #<zip object at 0x00A04CA8>, bu sorunla karşılaşmamak için;
print(list(names_and_heights))
# 5-Empty Lists
empty_list = []
# 6-Growing a List: Append
# Append komutu yardımıyla listenin sonuna eleman ekleyebiliriz, ancak sadece 1 tane eleman eklenebilir.
empty_list.append(1)
print(empty_list)
orders = ['daisies', 'periwinkle']
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)
# 7-Growing a List: Plus (+)
# Birden fazla veri eklemek istersek;
items_sold = ['cake', 'cookie', 'bread']
items_sold = items_sold + ['biscuit', 'tart'] # bunun yerine direk items_sold + ['biscuit', 'tart'] yapsaydık değişiklik olmazdı.
print(items_sold)
items_sold + ['ali', "als"] #todo bu niye olmadı?
# 8-Range I
# Range komutu ile sayılar üretebiliriz. Ancak zip komutunda olduğu gibi, hata ile karşılaşmamak için list komutunu kullanmalıyız.
list1 = range(9) #0,1,2,3,4,5,6,7,8 ==> 9'dan 1 eksik. ==> range(n) => 0..n-1
print(list1) #range(0, 9) output bu şekilde olacaktır.
print(list(list1))
# 9-Range II
my_range1 = range(2, 9)
print(list(my_range1))
my_range2 = range(2, 9, 2)
print(list(my_range2))
my_range3 = range(1, 100, 10)
print(list(my_range3))
## 2.2-Length of a List
# len komutu yardımıyla listenin eleman sayısını öğrenebiliriz.
my_list = [1, 2, 3, 4, 5]
print(len(my_list))
## 2.3-Selecting List Elements I
# Listedeki elemanları seçmek için;
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4=employees[4]
print(index4)
print(len(employees))
print(employees[6])
## 2.4-Selecting List Elements II
# Listedeki elemanları sondab başa doğru seçmek için ise - kullanılır.
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5, last_element)
## 2.5-Slicing Lists
# Listenin belli bir kısmını almak için => değişken=[start:end]
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:4]
print(beginning)
middle = suitcase[2:4] #[inclusive:exclusive]
print(middle)
## 2.6-Slicing Lists II
# Listenin en başından belli bir yere kadar olanı seçmek istiyorsak => değişken=[:x] gibi
# Listenin en sonundan belli bir yere kadar olanı seçmek istiyorsak => değişken=[x:] gibi
# Listenin son x rakamını seçmek istiyorsak => değişken=[-x:] gibi
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[-2:]
print(start,end)
## 2.7-Counting elements in a list
# Liste içindeki istenen ifadenin kaç tane olduğunu bulmak için count komutu kullanılır.
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake',
         'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count("Jake")
print(jake_votes)
print(votes.count("Cassie"))
## 2.8-Sorting Lists I
# sort komutu ile listelerin içindeki verileri nümerik ve alfabetik sıralayabiliriz.
# sort komutu kullanarak bir değişkene atayamayız, none çıktısı alırız.
# sort(değişken) gibi bir kullanım yoktur.
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
sorted_cities = cities.sort()
print(sorted_cities)
print(cities)
## 2.9-Sorting Lists II
# sort(değişken) gibi kullanımı yoktur, ancak listeleri sıraya koymak için diğer yöntem sorted komutudur. Bunda sorted(değişken) yapılabilir.
# yeni bir liste üretilebilir.
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted=sorted(games)
print(games_sorted)
print(games)
## 2.10-Review
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len=len(inventory)
print(inventory_len)
first=inventory[0]
last=inventory[-1]
inventory_2_6=inventory[2:6]
first_3=inventory[:3]
twin_beds=inventory.count("twin bed")
inventory.sort()
######################################## CODE CHALLENGES ##############################################################
#Write your function here
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#Write your function here
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList = sorted(unsorted)
  return sortedList

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Write your function here
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))