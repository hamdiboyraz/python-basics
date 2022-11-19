#https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-control-flow/cheatsheet

## 2-Boolean Expressions
#Nesnel olan bir cümle boolean olabilr, yani cevabı herkesce evet veya hayır olan cümlelerdir.

## 3-Relational Operators: Equals and Not Equals
# Bu operatörler iki değişkeni karşılaştırır. Doğruysa True, yanlışsa False döndürür.
# Eşit ise operatörü       : ==
# Eşit değil ise operatörü : !=
## 4- Boolean Variables
set_to_true = True
set_to_false = False
bool_one = 5 != 7       #True
bool_two = 1 + 1 != 2   #False
bool_three = 3 * 3 == 9 #True
my_baby_bool = "true"
print(type(my_baby_bool))     #<class 'str'>
my_baby_bool_two = True
print(type(my_baby_bool_two)) #<class 'bool'>
## 5-If Statements
# if durum1==durum2: (durum1, durum2 ye eşit ise altındaki komutları yap, değilse çık.)
#   print("bla bla")
def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"
user_name = "Dave"
print(dave_check(user_name))
## 6-Relational Operators II
#Büyüktür: >
#Küçüktür: <
#Büyük eşittir: >=
#Küçük eşittir: <=
def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"
def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"
print(graduation_reqs(120))
## 7-Boolean Operators: and
def graduation_reqs(credits,gpa):
  if (credits >= 120) and (gpa>=2):
    return "You meet the requirements to graduate!"
print(graduation_reqs(120,4))
# 8-Boolean Operators: or
def graduation_mailer(gpa, credits):
  if (gpa >= 2.0) or (credits >= 120):
    return True
print(graduation_mailer(2.7,140))
## 9-Boolean Operators: not
#not True == False
#not False == True
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"
print(graduation_reqs(3,80))
## 10-Else Statements
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."
## 11-Else If Statements
# Else If = Elif yapılarını programın sırayla kontrol etmesini sağlamak için kullanırız.
# Önce en baştaki if, daha sonra elif, en sonunda ise else yapısıyla sonlandırırız.
def grade_converter(gpa):
    grade = "F"
    if gpa >= 4.0:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"
    return grade     #Örneğin 3 ortalama ya sahip olsak, B,C,D,F koşulları da sağlanacak ancak sıraya koyduğumuz için hangisi doğru ise o aralığı uygular.
print(grade_converter(3))
## 12-Try and Except Statements
#Hata ile karşılaşıldığında fonksiyonu devam ettirmemizi sağlar.
def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:           #burda hatanın adı olması lazım,ValueError,NameError vs gibi
    print ("Can't divide by zero!")

########################################### CODE CHALLENGES ###########################################################

# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# Write your divisible_by_ten function here:
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

