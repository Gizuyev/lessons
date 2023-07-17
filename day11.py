# users ={
#     'name': 'Anton'
# }

# try:
#     print(a['age'])
# except KeyError as e:
#     print('Мы отловили keyError')
# except NameError as e:    

# else:
#     print('Все ок!')
# finally:
#     print('Обработка ошибок завершено')

# zero_except = 0
# while True:
#     try:
#         print(eval(input('>>> ')))
#     except ZeroDivisionError as e:
#         zero_except +=1
#         print('Не дели на ноль забаним сука!!!')
#     if zero_except == 3:
#         print('Вы забанены')

#Task 1
# import random


# while True:
#     number = random.randint(1,10)
#     try:
#         num = int(input(">>> "))
#     except ValueError:
#         print('Введите цифры')
#         continue
#     print(number)
#     if num == number:
#         print('Вы угадали')
#     else:
#         print('Вы не угадали')
       
#Task 2
# import random
# list = ['Natural', 'Gay', 'Supernatural', 'Eblan']
# rndm = random.choice(list)
# print(rndm)

#Task 3
# import random

# number = random.randint(1, 100)
# while True:    
#     try:
#         num = int(input('Угадайте число от 1 до 100: '))
#     except ValueError:
#         print('Вводи цифры тупоголовый!!!')
#         continue       
#     if num == number:
#         print('Ты угадал!!')
#     elif num > number:
#         print('Слишком много')
#     else:
#         print('Слишком мало')
#         continue           

#Task 4
# import random

# lst = []
# try:
#     s = random.choice(lst)
#     print(s)
# except IndexError:
#     print('Пустой лист')
            
#Task 5
# import random
# x = random.uniform(0, 1)
# y = random.uniform(0,1)
# print(x,y)

#Task 6
# import random
# lst = []
# try:
#     s = random.choice(lst)
#     print(s)
# except:
#     if lst == []:
#         print('Пустое значенине')

#Task 7
# import random

# nums = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# password = ''
# for i in range(10):
#     password += random.choice(nums)
# print(password)    

#Task 8
# import random
# while True:
#     num = int(input())
#     try:
#         s = random.randint(1, num)
#         print(s)
#     except ValueError:
#         print('Введите целое положительное число, ДУРЕНЬ!!!')
#     continue

#Task 9
# import random
# lst = ['1', '2', '7a', 'Natural', 'Bich', '888']
# try:
#     element = random.choice(lst)
#     print(int(element))
# except ValueError:
#     print('Объект невозможно преоброзовать в число, ЧУШКА ТУПАЯ')    

# Задачи с презентации их рот шатал!!!

#Task 1
# lst = ['1', '2', '7', '888']
# for i in lst:
#     print(lst[6])
#     s = i + 1
# print(g)    

#Task 2
# try:
#     lst = ['1', '2', '7', '888']
#     for i in lst:
#         # print(lst[6])
#         # s = i + 1
#         print(g) 
# except TypeError:
#     print('Еблан тупой разные же типы данных укурок !!!!!')
# except IndexError:
#     print('Out of range SUUUUUKAAAA! list не имеет такого индекса')
# except NameError:
#     print('Нет такого объекта НАРКОТ!!!!')

# Task 3
# lst = ['1', '2', '7', '888']
# for i in lst:
#     s = int(i) * 2
# print(s)    
# print(lst[3])

# Task 4
# try:
#     dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
#     for x in dict_.keys():
#         s =  x + 'abc'
#         print(s)
# except TypeError:
#     print('РАЗНЫЕ ТИПЫ ДАННЫХ НАРКОМАН')

#Task 5 
# try:
#     at = 10
#     it = 15
#     wo = 20
#     for e in range(-at, at):
#         print(wo / e)
#         if at > '5':
#             print('at > 5')
# except TypeError:
#     print('РАЗНЫЕ ТИПЫ ДАННЫХ')
# except IndexError:
#     print('OUT OF RANGE!!!! НЕТ такого индекса!!')
# except NameError:
#     print('the object does not exist!!')        

#Task 6
# lst = []
# for i in range(10):
#     lst.append(i)
# a = list(reversed(lst))
# sls_obj = slice(8)
# print(a[sls_obj])    

#Task 7
# a = 0
# b = 1
# numbers = []
# while b > a:
#     numbers.append(b)
# print(numbers)    
