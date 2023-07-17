#Task 1

#1.1

# def add(x: int, y: int):
#     return x + y

# print(add(2,2))

# 1.2

# def substract(x: int, y: int):
#     return x - y

# print(substract(2,2))

# 1.3

# def multiply(x: int, y: int):
#     return x * y

# print(multiply(2,2))

# 1.4
# def divide(x: int, y: int):
#     return x / y

# print(divide(2,2))

#Task 2
# def length(x: str):
#     count = 0
#     for i in x:
#         count += 1
#     return count

# print(length('Я натурал'))

#Task 3
# dict1 = {
#     'Shlak': 1,
#     'Block': 3,
#     'Bumerang': 'Rangbu'
#     }

# dict2 = {
#     'Barashek': 'Shon',
#     'Alkash': 'Brigada',
#     'Alkotest': 'Denny Phantom'
#     }


# def united(x,y):
#     x.update(y)
#     return x

# print(united(dict1, dict2))

#Task 4
# def order_list():
#     eat = input('Что вы хотели пожрать мудак? >>>> ')
#     drink = input('Пить что будешь чмо?>>>> ')
#     with open ('/home/ibragim/Рабочий стол/menu.txt', 'a') as file:
#         file.write(f'Жрать: {eat}\n')
#         file.write(f'Сушняк: {drink}\n')

# order_list()

#Task 5
# def creater():
#     name = input('Название хуйни которую ты хочешь создать: ')
#     file = open(name, 'a')

# creater()    

#Task 6
# def func1():
#     print('Я хуета ')
#     def func2():
#         print('Я параша')
#     func2()        

# print(func1())

#Task 7
# dict2 = {
#     'Barashek': 'Shon',
#     'Alkash': 'Brigada',
#     'Alkotest': 'Denny Phantom'
#     }

# def transform(n):
#     keyy = tuple(dict2.keys())
#     value = tuple(dict2.values())

#     return keyy, value 

# print(transform(dict2))

