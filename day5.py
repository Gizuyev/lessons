# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# list_1 = []
# list_2 = []
# if a % 2 == 0:
#     list_1.append(a)
# else:
#     list_2.append(a)
# if b % 2 == 0:
#     list_1.append(b)
# else:
#     list_2.append(b)
# if c % 2 == 0:
#     list_1.append(c)
# else:
#     list_2.append(c)
# if d % 2 == 0:
#     list_1.append(d)
# else:
#     list_2.append(d)
# if e % 2 == 0:
#     list_1.append(e)
# else:
#     list_2.append(e)
# print(list_1, list_2, sep='\n')

#Task 2
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# list_1 = []
# list_1.extend([a,b,c,d,e])
# print(max(list_1), min(list_1), sum(list_1) / len(list_1))

#Task 3
# a = int(input())
# products = ['яблоко', "груша", "арбуз", "банан", "мандарин"]
# print(products)
# if a > 4:
#     print('Нет такого индекса')
# else:
#     products.pop(a)
#     print(products)

#Task 4
# points = 0
# print('Самая большая гора в мире')
# print('a. Еверест', 'b. Эльбрус', 'c. Рашмор', sep='\n')
# answer_1 = input()
# if answer_1 == 'a':
#     points += 1
#     print('Вы заработали 1 балл.','Количество баллов', points)
# else:
#     points += 0
#     print('Ты тупой(ая)!')
# print('Скольго гендеров существует?')        
# print('a. 4', 'b. 2', 'c. 1', sep='\n')
# answer_2 = input()
# if answer_2 == 'b':
#     points += 1
#     print('Вы заработали 1 балл.','Количество баллов', points)
# else:
#     points += 0
#     print('Ты тупой(ая)!')
# print('Можно ли делить на ноль ?')
# print('a. Да', 'b. Возможно частично', 'c. Нет', sep ='\n')
# answer_3 = input()
# if answer_3 == 'c':
#     points += 1
#     print('Вы заработали 1 балл.','Количество баллов', points)
# else:
#     points += 0
#     print('Ты тупой(ая)!')
# print('Самый титулованный клуб Англии')
# print('a. Манчестер Юнайтед', 'b. Ливерпуль', 'c. Челси', sep='\n')
# answer_4 = input()
# if answer_4 == 'a':
#     points += 1
#     print('Вы заработали 1 балл.','Количество баллов', points)
# else:
#     points += 0
#     print('Ты тупой(ая)!')
# if points >= 3:
#     print('Вы прошли тест! Додик!')
# else:
#     print('Ты тупой!!!')    

# #Task 5
# list_1 = ['ироа', 'оамо', 'аорм', 'аорм', 'ао', 'омт', 'а', 'п', 'а', 'п']
# num = int(input())
# print(list_1[num:])

# #Task 6
# users = []
# a = input('Введите логин: ')
# b = input('Введите пароль: ')
# c = input('Подтвердите пароль: ')
# if not a.isdigit() and not a.isalpha():
#     print('Succes')
#     if b == c:
#         print('Вход выполнен')
#         users.extend([a,b])
#         print(users)   
#     else:
#         print('Пароли не совпадают')
# else:
#     print('Логин должен состоять из числ и букв')


