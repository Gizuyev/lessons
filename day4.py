# a = 'Hello world world hello'
# mid = len(a) // 2
# b = a[:mid] [::-1] + a[mid:]
# print(b)

# num1 = int(input())
# to_do = input()
# num2 = int(input())
# if to_do == '+':
#     print(num1 + num2)
# elif num2 == 0 and to_do == '/':
#     print('На ноль делить нельзя')     
# elif to_do == '-':
#     print(num1 - num2)
# elif to_do == '/':
#     print(num1 / num2)
# elif to_do == '*':
#     print(num1 * num2) 

# a, b = int(input()), int(input())
# s = a * b
# print('Площадь прямоугольника =', s)

# from math import sqrt
# a, b = int(input()), int(input())
# c = sqrt(a ** 2 + b ** 2)
# print(c)

# from math import *
# a = int(input())
# s = pi * a ** 2
# c = pi * a * 2
# print(c)

a, b, c = len(input()), len(input()), len(input())
if min(a,b,c) == b and max(a,b,c) == c:
    if c - a == a - b:
        print('YES')
        else:
            print('NO')
if min(a,b,c) == c and max(a,b,c) == a:
    if a - b == b - c:
        print('YES')
        else:
            print('NO')
if min(a,b,c) == b and max(a,b,c) == a:
    if a - c == c - b:
        print('YES')
    else:
            print('NO')
