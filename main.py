# tuple
# name = "Nurik"
# data = (1, 5, 2, 3, 4, 5, 6)
# print(name)
# print(data[5])
# print(data.count(5))
# print(data.count(8))
# print(len(data))
# print(data)
# print(data[1:4])
# for el in data:
#     print(el)


# sets
# Data = {1, 5, 2, 3, 4, 5, 6, }
# Name = set('nurmuhammad')
# print(name)
# Data.add(85)
# Data.update([8, 'Nurik'])
# Data.remove('Nurik')
# Data.clear()
# new_data = frozenset([7, 5, 2, 9, 'nurmuhammad'])
# print(new_data)
# print(Data)


# dict
# country = {1: 'Uzbekistan'}
# print(country[1])
# Country = {'code': 'Uzb', 'name': 'Uzbekistan', 'population': 36000000}
# print(country['name'])
# print(country['code'])
#  print(country['population'])
# new_country = dict(code='RU', name='Russian', population=144000000)
# print(new_country['name'])
# print(new_country['code'])
# print(new_country['population'])
# print(country , new_country)
# for el in country :
#    print(el)
# print(new_country.items())
# for key , value in country.items():
#     print(key , "-" , value)
# country.pop('name')
# country.clear()
# print(country.keys())
# print(country.values())
# country['code'] = Uzb sila
# person = {
#     'user_1': {'first name': 'Nurmuhammad',
#                'Surname': 'Shukurullaev',
#                'age': 23,
#                'address': ['Uzbekistan', 'Tashkent']
#                },
#     'user_2': {'first name': 'Ali',
#                'surname': 'Boburov',
#                'age': 43,
#                'address': ['Russia', 'moskva']
#                }
# }

# print(person['user_1']['address'][1])


# list
# nums = [5, 7, 2, 4, 7, 'true', 6.7]
# nums[1] = 23
# print(nums[4])
# nums.append(234)
# nums.insert(2, 8)
# nums.extend([6, 5, 4])
# nums.reverse()
# nums.pop()
# nums.remove('true')
# nums.clear()
# print(nums.count(7))
# print(len(nums))
# print(nums)
#                                               06.04.2024
#  Carname = 'Volvo'
# x = 50
# x = 5
# y = 10
#  print(x+y)
#  x, y, z = 'orange', 'banana', 'cherry'
#  x = y = 'orange'
#  z = x + y


# 1.text type =>string
# 2.number type => integer , float , complex
# 3.sequence type => list , tuple , range
# 4.mapping type => dict
# 5.set types =>set , frozenset
# 6.boolean types => bool => false and true
# 7.binary types => bytes , butearray, memoryview
# 8.none type => nonetype


# i = 1
# while i <= 11:
#      i += 1
#      if i == 7:
#         continue
# print(i)


# user = int(input("dayte chislo"))
# i = 0
# while i ** 2 <= user:
#      print(i ** 2)
#      i += 1
#
# user = int(input("dayte n chislo"))
# a = 2
# b = 1
# while a <=user:
#      a = a * 2
#      b = b + 1
# print(b - 1, a // 2)


# user = int(input("dayte n chislo"))
# a = 2
# b = 1
# while a <=user:
#     a = a * 2
#     b = b + 1
# print("uje nevozmojno")
# print(b - 1, a // 2)

# a = ["qovin", "taruz", "snickers", "cola", "chips"]
# for x in a:
#     print(x)
#     if x =="snickers":
#         break


# a = "     my name is Mirsaid"
# print(a.replace("Mirsaid" , "Nurmuhammad"))
# print(a.split(","))
# print(a.strip())
#
# a = "hello"
# b = "academy"
# print(a+' ' + b)

#
# a = "My name\'s Nurmuhammad"
# b = "My name\\s Nurmuhammad"
# c = "my name \n Nurmuhammad"
# print(a, b, c)

# x = "hello world"
# print(len(x))
# txt = "hello world"
# x = txt[0]
# print(x)
# x = txt[2:5]
# print(txt.strip())
# print(txt.upper())
# print(txt.lower())
# print(txt.replace("h" , "J"))
# age = 36
# txt = "my name is John, and I am {}"
# print(txt.format(age))
#
# def instagramm(*name):
#     print("amir likes => ", name[0]),
#     print("amir likes =>", name[1]),
#     print("alisher likes =>", name[2]),
#     print("mirafzal likes =>", name[3]),
#     print("ibragim likes =>", name[4]),
#     print("timur likes =>", name[5])
#
# instagramm("cristiano ronaldo", "messi", "meganfox", "lebron james", "mybeats", "jony sins" )
#
# def istagramm(**name):
#     print("", name["number"])
#
# istagramm(number=10, player='messi', game="dota 2", blogger="world_go_app")
#
# def istagramm(player = "ronaldiniyo"):
#     print("My favour player is", player)
#
# istagramm('Messi')
# istagramm("ronaldo")
# istagramm("penaldo")
#
# blogers = ["world_goo_app", " ", "mrbeast", "ishowspeed", "drake", "nelly furtado", "linkin park", "the weeknd", "image dragons", "bolalar"]
# def instagramm(followers):
#     for x in followers:
#         print(x)
# instagramm(blogers)
#
# def instagramm(x):
#     return 10 * x
#
# print(instagramm(5))
# print(instagramm(2))
# print(instagramm(4))
#
# instagramm = ("1)banana", "2)yabloki", "3)makaroni", "4)kofe")
# def blogers(followers):
#      for x in followers:
#          print(x)
# blogers(instagramm)

# classroom = ("1)baran", "2)joja", "3)joxori", "4)yayzo")
# def classmates(friends):
#    ssmates(classroom)
#  for x in friends:
#         print(x)

#
# def name(argument):
#     print(argument)
# name("i dont know python")
#
# def name(*,arguments):
#     print(arguments)
# name(arguments="qwerryy")

# def school(**name):
#     print(name['objects'])
# school(number = 43, classes = 344, objects = 28, person = 2098)
#
# def school(*name):
#     print('id like an ', name[1]),
# school('coffe', 'apple', 'bag', 'icecream')

# def recursiy(l):
#     if(l > 0):
#         overall = l + recursiy(l - 1)
#         print(overall)
#     else:
#         overall = 0
#     return overall
# print("recursiy method")
# recursiy(10)


# def my_function(*, my_function):
#     print(my_function)
# my_function(my_function = 'hello from a fuction')

# def school(**name):
#      print(name['classes'])
# school(number = 43, classes = 344)

# def my_function(*kids):
#     print("the youngest child is " , kids[2])
# my_function(3, 4, 7, 8)

#
# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial_recursive(n-1)
# print(factorial_recursive(6))
#
# a = lambda b : b + 1
# print(a(5))
#
# def a(b):
#     return b + 1
# print(a(5))
#
# kgh = lambda a : a
#
# def name(a):
#     return a**3 #a*a*a
# lam = lambda a : a ** 3
# while True:
#     b = input("vedite znacheniya dla a")
#     try:
#         a = int(b)
#         break
#     except ValueError:
#         print("error: vedite seloe chislo")
# print("result ->", name(a))
# print("result lambda function ->", lam(a))

# def a(b):
#     return b*b*b
# b = int(input("Enter a number"))
# print(a(b))

#
# cars = ['mers', 'bmw', 'audi', 'toyota', 'chevrolet']
# meal = ['plov', 'somsa', 'shashlik', 'burger', 'hotdog']
# city = ['tashkent', 'moskva', 'pekin' , 'paris', 'dubay']
# footballteam = ['real', 'barsa', 'manchester city', 'psg', 'alnassr']
#
# cars.extend(meal)
# cars.extend(city)
# cars.extend(footballteam)
# for x in cars:
#     print(x)
#

# game = ['pubg', 'brawl', 'fifa', 'contr']
# game.remove(game[2])
# game.append('fifa')
# game.reverse()
# game.insert(2, 'standoff')
# game.pop()
# for x in game:
#     print(game)

# a = [-10, -9, -8 -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in a:
#     if x % 2 == 0:
#        print(x)
#
# b = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# print(b)
#
# def change(lst):
#     # new_start = lst.pop()
#     # print(new_start)
#     # new_end = lst.pop(0)
#     # print(new_end)
#     lst.append(9)
#     lst.insert(2, 5)
#     print(lst)
#
# change([1,2,3,4])

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[2])
#
# a = [
#     [1,2,3,4,5]
# ]

# a = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8, 9, 0]
# ]
# print(a[1][4])

# b = [
#     [1, 2],
#     [
#         [3, 6, 7, 8],
#         [9, 10, 22, 33]
#     ]
# ]
# print(b[1][1][1])

# hello = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(hello[0])
# print(hello[9])
# print(hello[0]+hello[9])
# print(len(hello))
#
#
# a = [1, 2, 3, 4, 5, 6]
# print(a[0:3])
#
#
# run = 'abcde'
# for el in run:
#     print(el)

# data = {'year': '2025',
#         'month': '12',
#         'day': '31'}
#
# print(data['year'] + ' ' + data['month'] + ' ' + data['day'])
# b = range(1,100)
# print(b)
# a =  ['qweqw','sdgfdgdf','gdfgdfgfdg']
# a.reverse()
# print(a)

# for x in range(1, 101):
#     print(x)

# for x in range(-100, 0):
#     print(x)

# for x in range(101, 1, -1):
#     print(x)

# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)

# for x in range(1, 100):
#     if x % 3 == 0:
#         print(x)
#
# a = [1, 2, 3, 4, 5, 6]
# print(a[4:6])


# s = 'abcdef'
# a = s[0::2]
# print(a)  # Выведет: bdf
#
# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# print(a)
#
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst1.extend(lst2)
# print(lst1)
#
# a = [1, 3, 5, 7, 9]
# print(a)

# tpl1 = (1, 2, 3)
# tpl2 = (4, 5, 6)
# print(tpl1 + tpl2)

# dct1 = {
#     'a': 1,
#     'b': 2,
# }
# dct2 = {
#     'c': 3,
#     'd': 4,
# }
# dct1.update(dct2)
# print(dct1)

# st1 = {1, 2, 3, 4, 5, 6}
# st2 = {4, 5, 6, 7, 8}
#
# st1 = {1, 2, 3, 4, 5, 6}
# st2 = {4, 5, 6, 7, 8}
#
# common_elements = st1 & st2
# unique_common_elements = common_elements - (st1 - st2) - (st2 - st1)
#
# print(unique_common_elements)

# for i in range(1, 10, 2):
#     print(str(i) * i)

# for i in range(1, 10, 2):
#     print((str(i) * i).center(9))

# x = 1
# while x < 6:
#     x = x + 1
#     print(x)

# x = 1
# while x < 6:
#     x = x + 1
#     if x == 5:
#         break
#     print(x)

# x = 1
# while x < 10:
#     x = x + 1
#     if x == 3:
#         continue
#     if x == 5:
#             break
#     print(x)

# y = 1
# while y == 1:
#     x = input("what is your name?")
#     print("hello", x, ', welcome to bobir academy')

# x = int(input("celoy chislo"))
# while x != 0:
#     if x < 0:
#         print("мы встретили отрицательное число", x)
#         break
#     x = int(input("chislo ne otrisatelno"))
# else:
#     print("мы не встретили не одного отрицателбного числа")

# x = int(input("chislo"))
# y = 1
# while x > y:
#     x = x - 1
#     print(x)
#
# a = int(input("chislo"))
# d = 1
# while a > d:
#     a = a - 1
#     print(a)
#
# x = 1
# y = int(input("chislo"))
# while x < y:
#     x = x + 1
#     if x == y:
#         break
#     print(x)
#
# print(x + a)
#
# x = int(input("chislo"))
# y = 2
# while x > y:
#     y = y * y
#     if x == 1000:
#         break
#     print(y)

# x = int(input("chislo"))
# y = 3
# while x > y:
#     y = y * y
#     if x == 1000:
#         break
#     print(y)
#
# for x in range(1, 20):
#     print(x)

# for i in range(2, 10, 2):
#     print(str(i) * i)
#
# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# print(a[0][0], a[0][1], a[0][2])
# print(a[1][0], a[1][1], a[1][2])
# print(a[2][0], a[2][1], a[2][2])
#
# for i in range(1, 10, 2):
#     print(str(i) * i)

# for i in range(1, 10, 1):
#     print(str(i) * 3)

# events = [
#   {
#     'date':  '2019-12-29',
#     'event': 'name1'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name2'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name3'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name4'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name5'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name6'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name7'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name8'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name9'
#   },
# ]
#
# MyBox = {}
# for event in events:
#   date = event['date']
#   event_n = event['event']
#   if date not in MyBox:
#     MyBox[date] = [event_n]
#   else:
#     MyBox[date].append(event_n)
# print(MyBox)

# lst = ['abcd', 'ab', 'c', 'de', 'bc']
# lst1 = filter(lambda x: len(x) == 2, lst)
# print(list(lst1))
#
# for lst1 in lst:
#     if len(lst1) == 2:
#         print(lst1)






# #Разделить строку
# my_string = "Пример строки для разделения"
# parts = my_string.split()
# print(parts)
#
# #Как найти индекс символа в строке
# salamaleykum = "Hello, NIggaz"
# index = salamaleykum.index("o")
# print(index)
#
# #Объединить строки
# strings = ["Привет", "мир"]
# result = " ".join(strings)  # Объединение строк из списка с пробелом между ними
# print(result)
#
# name = "John"
# age = 30
# result = f"Привет, меня зовут {name} и мне {age} лет."
# print(result)  # Выведет: "Привет, меня зовут John и мне 30 лет."
# # or just '+'
#
# #Заменить часть строки
# my_string = "Это пример строки"
# new_string = my_string.replace("пример", "новый пример")
# print(new_string)  # Выведет: "Это новый пример строки"
#
# #Удалить пробелы в строке
# my_string = "Это строка с пробелами"
# new_string = my_string.replace(" ", "")  # Удаление всех пробелов из строки
# print(new_string)  # Выведет: "Этострокаспробелами"
#
# my_string = "   строка с пробелами   "
# new_string = my_string.strip()  # Удаление пробелов с обоих концов строки
# print(new_string)  # Выведет: "строка с пробелами"
#
# my_string = "   строка с пробелами   "
# left_stripped = my_string.lstrip()  # Удаление пробелов слева
# right_stripped = my_string.rstrip()  # Удаление пробелов справа
# print(left_stripped)  # Выведет: "строка с пробелами   "
# print(right_stripped)  # Выведет: "   строка с пробелами"
#
# #Удалить символы в строке
# my_string = "Это строка с символами"
# new_string = my_string.replace("с", "")  # Удаление символа "с" из строки
# print(new_string)  # Выведет: "Это трока иимволами"
#
# my_string = "Это строка с символами"
# chars_to_remove = ['с', 'и']
# new_string = "".join(char for char in my_string if char not in chars_to_remove)  # Удаление символов "с" и "и"
# print(new_string)  # Выведет: "Это трока  символам"
#
# #Удалить последний символ в строке
# my_string = "Пример строки для удаления последнего символа"
# new_string = my_string[:-1]  # Удаление последнего символа с помощью среза
# print(new_string)  # Выведет: "Пример строки для удаления последнего символ"
#
# my_string = "Пример строки для удаления последнего символа"
# new_string = my_string.rstrip(my_string[-1])  # Удаление последнего символа с помощью метода rstrip()
# print(new_string)  # Выведет: "Пример строки для удаления последнего символ"
#
# #Удалить первый символ в строке
# my_string = "Пример строки для удаления первого символа"
# new_string = my_string[1:]  # Удаление первого символа с помощью среза
# print(new_string)  # Выведет: "ример строки для удаления первого символа"
#
# my_string = "Пример строки для удаления первого символа"
# new_string = my_string.lstrip(my_string[0])  # Удаление первого символа с помощью метода lstrip()
# print(new_string)  # Выведет: "ример строки для удаления первого символа"
#
# my_string = "Пример строки для удаления первого символа"
# new_string = my_string.replace(my_string[0], "", 1)  # Удаление первого символа с помощью метода replace()
# print(new_string)  # Выведет: "ример строки для удаления первого символа"
#
# #Удалить строку
# my_string = "Это строка для удаления"
# del my_string  # Удаление переменной, содержащей строку
#
# my_string = "Это строка для удаления"
# my_string = None  # Присвоение переменной значения None

# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)

# i = 1
# while i < 6:
#   print(i)
#   i += 1


# x = 0
# while x < 10:
#     x = x + 1
#     if x == 11:
#         break
#     print(x)

# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)

# for x in range(1, 10):
#     if x % 2 == 1:
#         print(x)

# num = 1
# while num < 10:
#     num = num + 2
#     print(num)

# a = {1, 2, 3, 4, 5, 6, 12, 24}
# a.remove(12)
# print(a)

# a = {1, 2, 3, 4, 5, 6, 12, 24}
# a.remove(3)
# a.remove(5)
# a.remove(6)
# a.remove(12)
# a.remove(24)
# a.add('apple')
# a.add('john')
# a.add('cs')
# a.add('mango')
# a.add('grapes')
# print(a)

# a = {96, 65, 2, 'joseph'}
# b = {1, 'peter', 59}
# a.update(b)
# print(a)


# def dobavit():
#     a = {'Rassiya', 'Uzbekistan', 'Kitay'}
#     x = input('dayte stranu')
#     a.add(x)
#     print(a)


# def remov():
#     a = {'Rassiya', 'Uzbekistan', 'Kitay'}
#     x = input('udalite stranu')
#     a.remove(x)
#     print(a)


# def over():
#     f = int(input("0 mi yoki 1"))
#     if f == 1:
#         dobavit()
#     elif f == 0:
#         remov()
# over()            

# def text_man():
#     print('this is man')

# def text_woman():
#     print('this is woman')

# def result():
#     a = int(input('choose one number 1 => man , 2 => woman'))
#     if a == 1:
#         text_man()
#     if a == 2:
#         text_woman()
# result()

# def text_number():
#     print(range(0, 11))

# def text_alphabet():
#     print('a, b, c, d, e')

# def result():
#     a = int(input('viberity metod obsheniya 1 = > number , 2 => alphabet'))
#     if a == 1:
#         text_number()
#     if a == 2:
#         text_alphabet()    
# result()




# class Myacademy:
#     man = 10
#     a = input('pointer')
#     def name (self):
#         print('my name is david')
# p = Myacademy()                 
# print(p.man)
# print(p.a)
# p.name()

# class Myacedemy:
#     man = 10

#     def __init__(self,type,age,lang):
#         self.type = type
#         self.age = age
#         self.lang = lang

#     def __str__(self):
#         return f"{self.type}({self.age})({self.lang})"

#     # def name(self):
#     #     print('My name is David')

# p = Myacedemy('man',35,'uz')
# c = Myacedemy('women',25,'ru')
# print(p)
# print(c)

# class Behruz:

#     def __init__(self, name , country, data_of_birth):
#         self.name = name
#         self.country = country
#         self.data_of_birth = data_of_birth

# b = Behruz('bexruz', 'tashkent', '14')

# print("his name is", b.name, "hi was born", b. data_of_birth, "he is from", b.country)




# from datetime import date

# class BexruzFamily:

#     def __init__(self,name,country,data_of_birth):
#         self.name = name
#         self.country = country
#         self.data_of_birth = data_of_birth

#     # def bexruz(self):
#     #     self.name = 'Bexruz'
#     #     self.country = "Tashkent"
#     #     self.data_of_birth = 14
#     #     return f"His name is,{self.name},He was born in "
#     #     {self.country}
#     #     "He is ", {self.data_of_birth}, " years old"
#     #
#     # def pet(self):
#     #     self.name = 'Chixaxu'
#     #     self.country = "Tashkent"
#     #     self.data_of_birth = 1
#     #     return f"His pets name is,{self.name},it was born in "
#     #     {self.country}
#     #     "it is ", {self.data_of_birth}, " years old"
#     # def __init__(self,name,country,data_of_birth):
#     #     self.name = name
#     #     self.country = country
#     #     self.data_of_birth = data_of_birth

# b = BexruzFamily('Bexruz','Tashkent',14)
# a = BexruzFamily('Chixaxu','Tashkent',1)
# # b = BexruzFamily('')
# # print(b.bexruz())
# # print(b.pet())
# print("His name is ", b.name,
#       "He was born in ", b.country,
#       "He is ",b.data_of_birth," years old")

# print("His name is ", a.name,
#       "He was born in ", a.country,
#       "He is ",a.data_of_birth," years old")

# from datetime import date
# class  person:
#     def __init__(self, name, country, data_of_birth, age):
#         self.name = name
#         self.country = country
#         self.data_of_birth = data_of_birth
#         self.age = age
# a = person('Ferdi Odilia', 'france', 1962-7-12, 60)
# b = person('shweta maddox', 'canada', 1982-10-20, 40)
# c = person('elizaveta timan', 'usa', 2000-1-1, 23)
# print("His name is ", a.name,
#        "He was born in ", a.country,
#       "He is ",a.data_of_birth," years old")
# print("His name is ", b.name,
#        "He was born in ", b.country,
#        "He is ",b.data_of_birth," years old")
# print("His name is ", c.name,
#        "He was born in ", c.country,
#       "He is ",c.data_of_birth," years old")



# a = 0 
# b = int(input("give me a number"))
# if a < b:
#        print(1)
# elif a > b:
#        print(-1)
# elif a == b:
#        print(0)
# else:
#        print('nenenen')

# print('scolko budet 1 + 1')
# while True:
#        a = int(input('give me a number'))
#        if a == 2:
#               print('true')
#               break
#        elif a < 2:
#               print('notori')
#        elif a > 2:
#               print('false')
#        else:
#               print('povtorite zanovo')

# a = range(0, 10)
# for x in a:
#     if x == 6:
#         break
    
#     print(x)
# print('yettim 6') 

# print('dayte login i parol')
# while True:
#     a = str(input('login'))
#     b = str(input('dayte parol'))
#     if a == 'qwerty' and b == 'qwerty':
#         print('true')
#         break
#     elif a != 'qwerty' and b != 'qwerty':
#         print('its false')
#         break
# else:
#     print('zanovo')


# print("dayte chislo")
# while True:
#     a =input('chislo')
#     if a % 2 == 0 :
       
#        print('chislo chotno')
#     if a % 2 == 1 : a < b >
#        print('chislo nechetno')  
# else:
#     print('zanovo')

# number = 8757
# a = list(str(number))
# print(a[0])

# print('chetiroxznachoe chislo')
# while True:
#     a = int(input('dayte chislo'))
#     if 999 < a  and a < 10000:

#        a = list(str(a))
#        if a[0] == a[1] or a[0] == a[2] :
#            print(True)
#            break
#        elif a[3] == a[1] or a[3] == a[2]:
#            print('true')
#            break
# else :
#     print('zanova')

# print('scolco let')
# while True:
#     a = int(input('let:'))
#     if a < 16:
#         print('dostup zapreshen')
#     elif a > 16:
#         print('dostup otkrit')    
#         break
# else:
#     print('zanovo')

# print('zadayte chislo')
# while True:
#     a = int(input('1 chislo'))
#     b = int(input('2 chislo'))
#     c = int(input('3 chislo'))
#     if a - b == b - c:
#         print('true')
#         break
#     elif a - b != b - c:
#         print('false') 
# else:
#     print('zanovo')           

# class familybexruz:
#     @staticmethod
#     def is_age(age):
#         age = 15
#         if age > 18:
#             print("True")
#         else:
#             print("False")

# def spalniy(self, b):
#     self.b = b
#     print("this is simple method", self.b)    

# class familysalima(familybexruz): 
#     pass


# a = familysalima()
# a.spalniy(20)
# a.is_age(20)


# class vihecle:
#     def __init__(self, name, mile, capacity ):
#        self.name = name
#        self.mile = mile
#        self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100     
# class bus(vihecle):
#     pass
# b =bus('daughter', 10, 50 )
# print('stoimost avtobusa', b.fare())

class A:
    def pay_for_cal(dollar):
        if 
    def slesh(self, a, b):
        return a + b + 2
    def prosent(self, a, b):
        return a + b - 2 
    def add(self, a, b):
        return a + b 
    def minus(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b 
    def div(self, a, b):
        return a / b 
    
cal = A()
def input_ask():
    x = int(input('1 chislo'))
    y = int(input('2 cjislo'))
    return x, y 

symbol = input("viberite (+  -  *  /  %  !)")

if symbol in ['+', '-', '*', '/', '!', '%']:
    num1, num2 = input_ask()

    if symbol == '+':
        print('resultat:', cal.add(num1, num2))
    if symbol == '-':
        print('resultat:', cal.minus(num1, num2))
    if symbol == '*':
        print('resultat:', cal.mult(num1, num2))
    if symbol == '/':
        print('resultat:', cal.div(num1, num2))
    if symbol == '!':
          print('resultat:', cal.slesh(num1, num2))  
    if symbol == '%':
          print('resultat:', cal.prosent(num1, num2))        


































































































































