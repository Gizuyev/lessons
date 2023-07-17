# import datetime

# # today = datetime.date.today()
# # now = datetime.datetime.now()

# now = datetime.datetime.now()
# formated_date = now.strftime('Год: %Y месяц: %m день:%d')
# print(formated_date)

# import os
# import sys
# import random


# print(os.name)
# print(sys.platform)
# print(random.choice(['name1', 'name2', 'name3', 'name4']))

# Task 1
# from name import data
# print(data)

# Task 2
# import random
# lst = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# lst2 = []
# for i in range(4):
#     s = random.choice(lst)
#     lst2.append(s)
# print(lst2)

# Task 3
# import sys
# print(sys.platform)

# Task 4
# import sys 

# print(sys.argv)
# if sys.argv == 69:
#     print('Ты натурал')
# else:
#     print('Ты гей!!')    

# Task 5
# import os
# import random
# for i in range(5):
#     os.system(f'touch /home/ibragim/"Рабочий стол"/folder/newfile{i}.txt')

#Task 6
# import random

# lst = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# ragnarok = []
# akatsuki = []
# bichi = []
# alkash_brigada = []
# while len(lst) != 1:
#     t1 = random.choice(lst)
#     ragnarok.append(t1)
#     lst.remove(t1)
#     t2 = random.choice(lst)
#     akatsuki.append(t2)
#     lst.remove(t2)
#     t3 = random.choice(lst)
#     bichi.append(t3)
#     lst.remove(t3)
#     t4 = random.choice(lst)
#     alkash_brigada.append(t4)
#     lst.remove(t4)
# print(f'Игрок {lst} лох')
# print(ragnarok)
# print(akatsuki)
# print(bichi)
# print(alkash_brigada)

#Task 7
# import sys
# a, b = input(), input()
# a1 = sys.getsizeof(a)
# b2 = sys.getsizeof(b)
# if a1 > b2:
#     print('Первый объект тяжелее')
# else:
#     print('Второй объект весит больше')    

#Task 8
# import random
# from string import ascii_letters, digits
# passl = int(input('Введите длину пароля: >>> '))
# password = ''
# for i in range(passl):
#     s = random.choice(ascii_letters)
#     password += s
# print(password)    

#Task 9
# import random
# s = random.randrange(6, 12)
# y = random.randrange(5,100,5)
# print(s, y)

#Task 10
# from datetime import datetime, timedelta
# date = datetime.now().date()
# will_be = date + timedelta(days=1000)
# print(will_be)
#-------------------------------------------------

#Task 8
# from datetime import datetime, timedelta
# date = datetime.now().date()
# print(f'Текущая дата: {date}')
# add = int(input('Сколько дней добавить к текущей дате: >>> '))
# will_be = date + timedelta(days=add)
# print(will_be)

#Task 9
# import random 
# s = random.randrange(1, 100)
# with open ("database.txt", 'a') as file:
#     save = file.write(str(s))

