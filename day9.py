#Task 1
# login = input()
# password = input()
# with open('main.txt', 'a') as file:
#     file.write(f"Логин:{login}\n Пароль:{password}\n")

#TasK 2
# with open('main.txt', 'r') as file:
#     if 'w' in file.read():
#         print('Буква "W" есть в файле')
#     else:
#         print('Буква "W" нет в файле')    

#Task 3        
# t_words = []
# with open('main.txt', 'r') as file:
#     text = file.read()
#     for i in text.split():
#         if "t" in i or "T" in i:
#             t_words.append(i)
# print(t_words)        

#Task 4
# while True:
#     sign_log_in = input('1. Вход: '
#                         '2. Регистрация: ')
#     if sign_log_in == '1':
#         login = input('Введите логин: ')
#         password = input('Введите пароль: ')
#         with open('main.txt') as file:
#             data_base = file.read()
#             if login in data_base and password in data_base:
#                 print('Вы успешно вошли в аккаунт !')
#             else:
#                 print('Неверный логин или пароль')
#     elif sign_log_in == '2':
#         login = input('Придумайте логин: ')
#         password = input('Придумайте пароль: ')
#         password_repeat = input('Повторите пароль: ')
#         with open('main.txt', 'r') as file:
#             data_base = file.read()
#             if login in data_base and password in data_base:
#                 print('У вас уже есть аккаунт на сайте гей знакомств')
#             elif password == password_repeat:
#                 print('Вы успешно зарегистрировались на сайте гей знакомств')
#                 with open('main.txt', 'a') as file:
#                     file.write(f'Логин: {login}\n Пароль: {password}\n')

#Task 5
# while True:
#     login = input('1. Придумайте логин: ')
#     password = input('2. Придумайте пароль: ')
#     password_repeat = input('3. Повторите пароль: ')
#     image = input('3.Загрузите изображение указав путь до него: ')
#     with open('database.txt', 'a', encoding='utf-8') as file:
#         save = (file.write(f'login: {Login}\n Password: {password}\n image: {image}\n'))







