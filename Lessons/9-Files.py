## https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-files/cheatsheet

## 1-Reading a File
# with as komutu ile dosyaları python ile açabiliriz.
# with open('dosya adı) as python_kodunda_kullanacagımız_ad:
"""with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)"""

## 2-Iterating Through Lines
# dosya içindeki her bir satırdakini ayrı ayrı okur ve yazdırır.
"""with open("how_many_lines.txt") as lines_doc:
    for i in lines_doc.readlines():
        print(i)"""

## 3-Reading a Line
# readline, tek tek okur, second_line diye altına yazsak, text dosyasındaki ikinci satırı yazacak
"""with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)"""

## 4-Writing a File
# w nin yerinde normalde, yani defaultta r vardır. biz w yazarak r yi w ile değiştiriyoruz. dosyaya yazma işlemini gerçekleştiriyoruz.
"""with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("sea")"""

## 5-Appending to a File
# r yerine bu kez a yazıyoruz, yani append'in a sı
"""with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")"""

## 6-What's With "with" ?
# with ile kullandığımızda içine kodları yazdığımızda fonksiyondaki gibi, içerisinde kalır, yani dosyayı açar ve kapatır.
# with in alternatif çözümü şu şekildedir
"""close_this_file = open('fun_file.txt')

setup = close_this_file.readline()
punchline = close_this_file.readline()

print(setup)"""
# ancak açıp kapatmak hatalara sebep olcağı için with kullanışlıdır.
"""with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()
print(setup)"""

## 7-What Is a CSV File? #https://docs.python.org/3/library/csv.html#id3
# python text dosyaları dışında csv dosyalarını da açabilir. csv dosyası = comma seperated values  virgülle ayrılmış değerler
# excelde mesela başlıklarla kolonları arasına virgül koyarak oluşturmak
"""with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())"""

## 8-Reading a CSV File
# CSV dosyasından verileri almak için önce import ile kütüphanemizi çektik, daha sonra with komutuyla dosyayı açtık.
# csv.DictReader ile dosyayı okuttuk.
# iterasyon ile dosyadaki belirli bir başlıktaki (cool fact) verileri çektik
"""import csv
with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for i in cool_csv_dict:
    print(i["Cool Fact"])"""

## 9-Reading Different Types of CSV Files

"""import csv

with open('books.csv') as books_csv:  # burda da bazen books.csv",newline="" konuyor bunu da anlamadım
  books_reader = csv.DictReader(books_csv,delimiter='@') # burda delimiter yazmazsak sadece "@" yazarsak hata oluyor, sebebini anlamadım.
  isbn_list = [i['ISBN'] for i in books_reader]"""

## 10-Writing a CSV File
#
"""access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for i in access_log:
    log_writer.writerow(i)"""

## 11-Reading a JSON File
# javascript ile ilgili pythonun geliştirdiği özel bir modün json
"""import json
with open("message.json") as message_json:
  message = json.load(message_json)
print(message)"""

## 12-Writing a JSON File
"""data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json
with open("data.json","w") as data_json:
  json.dump(data_payload,data_json)"""

