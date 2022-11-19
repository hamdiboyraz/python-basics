## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-function-arguments/cheatsheet

## 1-Parameters and Arguments

#A parameter is a variable in the definition of a function.
#An argument is the value being passed into a function call.
#A function definition begins with def and contains the entire following indented block.
#And function calls are the places a function is invoked, with parentheses, after its definition

# The "def" keyword is the start of a function definition
def function_name(parameter1, parameter2):
  # The placeholder variables used inside a function definition are called parameters
  print(parameter1)
  return parameter2
# The outdent signals the end of the function definition

# "Arguments" are the values passed into a function call
argument1 = "argument 1"
argument2 = "argument 2"

# A function call uses the functions name with a pair of parentheses
# and can return a value
return_val = function_name(argument1, argument2)

from record_library import place_record, rotate_record, drop_needle

def play_record(album):
  place_record(album)
  rotate_record(album)
  drop_needle(album)

next_album = "Blondie / Parallel Lines"

play_record(next_album)

#The name of the parameter is album. The name of the argument is next_album.

## 2-None: It's Nothing!
# None, özel bir ifadedir, bir değerin None' a eşit olup olmadığını kontrol edip, if döngülerimizi yönlendirebiliriz.
none_var = None
if none_var:
  print("Hello!")
else:
  print("Goodbye")

# Prints "Goodbye"

# first we define session_id as None
session_id = None

if session_id is None:
  print("session ID is None!")
  # this prints out "session ID is None!"

# we can assign something to session_id
if active_session:
  session_id = active_session.id

# but if there's no active_session, we don't send sensitive data
if session_id is not None:
  send_sensitive_data(session_id)

from review_lib import get_next_review, submit_review

# define review here!
review = get_next_review()
if review is not None:
  submit_review(review)

## 3-Default Return

def no_return():
  print("You've hit the point of no return")
  # notice no return statement

here_it_is = no_return()

print(here_it_is)
# Prints out "None"

# store the result of this print() statement in the variable prints_return
print("What does this print function return?")

# print out the value of prints_return
prints_return = print("hi!")
print(prints_return)

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()

# print out the value of list_sort_return
print(list_sort_return)

## 4-Default Arguments

# Function definition with two required parameters
def create_user(username, is_admin):
  create_email(username)
  set_permissions(is_admin)

# Function call with all two required arguments
user1 = create_user('johnny_thunder', True)

# Raises a "TypeError: Missing 1 required positional argument"
user2 = create_user('djohansen')

# Function defined with one required and one optional parameter
def create_user(username, is_admin=False):
  create_email(username)
  set_permissions(is_admin)

# Calling with two arguments uses the default value for is_admin
user2 = create_user('djohansen')

# We can make all three parameters optional
def create_user(username=None, is_admin=False):
  if username is None:
    username = "Guest"
  else:
    create_email(username)
  set_permissions(is_admin)

# So we can call with just one value
user3 = create_user('ssylvain')
# Or no value at all, which would create a Guest user
user4 = create_user()

## 5-Using Keyword and Positional Arguments

# Raises a TypeError
def create_user(is_admin=False, username, password):
  create_email(username, password)
  set_permissions(is_admin)

# Works perfectly
def create_user(username, password, is_admin=False):
  create_email(username, password)
  set_permissions(is_admin)

## 6-Keyword Arguments

# Define a function with a bunch of default arguments
def log_message(logging_style="shout", message="", font="Times", date=None):
  if logging_style == 'shout':
    # capitalize the message
    message = message.upper()
  print(message, date)

# Now call the function with keyword arguments
log_message(message="Hello from the past", date="November 20, 1693") #message=.. olarak yazdıgımız için, değişkeni ilk sıradaki değişken olarak algılamadı.
import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
  shape = shapes.draw_shape(shape_name, character)
  if not line_breaks:
    print(shape[1:-1])
  else:
    print(shape)

# call draw_shape() with keyword arguments here:
draw_shape(character = "m", line_breaks = False)

## 7-Don't Use Mutable Default Arguments
# list gibi verileri değişen argümanlar kullanma, int float string tuple vs kullanılır bunlar immutabledir yani değişmez
def populate_list(list_to_populate=[], length=1):
  for num in range(length):
    list_to_populate.append(num)
  return list_to_populate

returned_list = populate_list(length=4)
print(returned_list)
# Prints [0, 1, 2, 3] -- this is expected

returned_list = populate_list(length=6)
print(returned_list)
# Prints [0, 1, 2, 3, 0, 1, 2, 3, 4, 5] -- this is a surprise!

## 8-Using None as a Sentinel
# yukardaki durumu düzeltmek için None dan yardım alıyoruz
def add_author(authors_books, current_books=None):
  if current_books is None:
    current_books = []

  current_books.extend(authors_books)
  return current_books

def update_order(new_item, current_order = None):
  if current_order is None:
    current_order = []
  current_order.append(new_item)
  return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)

## 9-Unpacking Multiple Returns

def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums
sum_and_div = multiple_returns(20, 10)

print(sum_and_div)
# Prints "(30, 2)"

print(sum_and_div[1])
# Prints "30"

sum, div = sum_and_div(18, 9)

print(sum)
# Prints "27"

print(div)
# Prints "2"

def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("Hello")
print(the_scream) #HELLO
print(the_whisper) #hello
print(the_scream, the_whisper) #HELLO hello
print(scream_and_whisper("Hello")) #('HELLO', 'hello') bunun cıktısı tuple oluyor galiba
print(scream_and_whisper("Hello")[0]) #HELLO
print(scream_and_whisper("Hello")[1]) #hello

## 10-Positional Argument Unpacking
def shout_strings(*args):
  for argument in args:
    print(argument.upper())

shout_strings("hi", "what do we have here", "cool, thanks!")
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"

def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])

truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# Prints out:
# "What's g"
# "Looks li"

from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += '/' + arg
  return joined_string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))

## 11-Keyword Argument Unpacking

# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(
	name="Tim",
  feeling="10/10",
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  Baseball='3',
  Shirt='14',
  Guitar='70')

## 12-Using Both Keyword and Positional Unpacking
#All named positional parameters
#An unpacked positional parameter (*args)
#All named keyword parameters
#An unpacked keyword parameter (**kwargs)

def main(filename, *args, user_list=None, **kwargs):
  if user_list is None:
    user_list = []

  if '-a' in args:
    user_list = all_users()

  if kwargs.get('active'):
    user_list = [user for user_list if user.active]

  with open(filename) as user_file:
    user_file.write(user_list)

main("files/users/userslist.txt",
     "-d",
     "-a",
     save_all_records=True,
     user_list=current_users)

filename == "files/users/userslist.txt"
args == ('-d', '-a)
user_list == current_users
kwargs == {'save_all_records': True}


def remove(filename, *args, **kwargs):
    with open(filename) as file_obj:
        text = file_obj.read()
    for arg in args:
        text = text.replace(arg, "")
    for kwarg, replacement in kwargs.items():
        text = text.replace(kwarg, replacement)

    return text


print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))

## 13-Passing Containers as Arguments

def takes_many_args(*args):
  print(','.join(args))

long_list_of_args = [145, "Mexico City", 10.9, "85C"]

# We can use the asterisk "*" to deconstruct the container.
# This makes it so that instead of a list, a series of four different
# positional arguments are passed to the function
takes_many_args(*long_list_of_args)
# Prints "145,Mexico City,10.9,85C"

def pour_from_sink(temperature="Warm", flow="Medium")
  set_temperature(temperature)
  set_flow(flow)
  open_sink()

# Our function takes two keyword arguments
# If we make a dictionary with their parameter names...
sink_open_kwargs = {
  'temperature': 'Hot',
  'flow': "Slight",
}

# We can destructure them an pass to the function
pour_from_sink(**sink_open_kwargs)
# Equivalent to the following:
# pour_from_sink(temperature="Hot", flow="Slight")
from products import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

new_product_dict = {
  'Apple': 1,
  'Ice Cream': 3,
  'Chocolate': 5,
}

# Call create_product() by passing new_product_dict
# as kwargs!

create_products(**new_product_dict)

