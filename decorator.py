# def get_sq(func):
#     def ochko(*args,**kwargs):
#         print(f'Площадь треугольника:{func(*args,**kwargs)}')
#     return ochko
        

# @get_sq
# def ggg(x,n):
#     return x * n

# ggg(2,2)
  
# Задачи с презентации >>>>>>>>>>>>>>>>>>>>>>>>

# import random

# def decorate(func):
#     def inner():
#         result = func()
#         return set(result)
#     return inner

# @decorate
# def generate():
#     lst = []
#     for i in range(100):
#         lst.append(random.randint(10,50))
#     return lst

# print(generate())
import random

def shif(func):
    def wrap():
        s = func()
        return ord(s)
    return wrap 


@shif
def log_pass():
    login = list(input('Придумайте логин: '))
    password = list(input('Придумайте пароль: '))
    return login, password

print(log_pass())





