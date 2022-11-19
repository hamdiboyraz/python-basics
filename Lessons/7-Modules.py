## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-modules/cheatsheet

## 1-Modules Python Introduction
# kütüphaneden veri cekmeye yarar.
from datetime import datetime
current_time=datetime.now()
print(current_time)

## 2-Modules Python Random
# random.randint(a,b) => a ile b arasında sayı üretir. b dahil değil.
# random.choice(değişken) => içinden rastgele sayıyı seçer.
# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]
print(random_list)
# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

## 3-Modules Python Namespaces
# kütüphaneden çektiğimiz modül adını "as" ile projemizde farklı bir isim ile kullanabiliriz.
"""import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt

import random

numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()"""

## 4-Modules Python Decimals

# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
two_decimal_points_decimalsiz = 0.2+0.69
print(two_decimal_points)
print(two_decimal_points_decimalsiz)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

## 5-Modules Python Files and Scope
# Başka python dosyalarındaki fonksiyonları çağırabiliriz.

#library.py
# Add your always_three() function below:
def always_three():
  return 3
# Import library below:
#from library import always_three ==> yukardaki library.py dosyasından always_three fonksiyonunu çağırıyoruz.
# Call your function below:
always_three()

############################################  VIDEO-1 DATETIMES #######################################################
from datetime import datetime
birthday=datetime(1995,5,16,8,0)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.minute)
print(birthday.weekday())
print(datetime.now())
print(datetime(2021,1,1)-datetime(2020,1,1))
print(datetime(2020,1,1)-datetime(2019,1,1))
print(datetime.now()-datetime(2018,6,22))
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y') #https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes
print(parsed_date)
print(parsed_date.day)
print(parsed_date.month)
print(parsed_date.year)
date_string = datetime.strftime(datetime.now(),'%b %d, %Y')
print(date_string)

#################################################  VIDEO-2