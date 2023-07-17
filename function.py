# def sqrt_of_num(x):
#     print(x ** 2)

# sqrt_of_num(2)

# import random
# def rand_nums():
#     nums = '123456789'
#     lst = []
#     for i in range(10):
#         lst.append(random.choice(nums))
#     return ''.join(lst)    
    
# print(rand_nums())

#Task 3
# lst = [1,2,3]
# def sum_massive(x):
#     return sum(x)
    
# print(sum_massive(lst))

#Task 4
# def reverse_str(x):
#     return x[::-1]

# print(reverse_str('Я натурал'))

#Task 5
# def palindrom(x):
#     if x[::-1] == x:
#         return 'Palindrome'
#     else:
#         return 'Not palindrome'

# print(palindrom('LOL'))    

#Task 6
# def trans(x):
#     y = ''
#     while x > 0:
#         s = x % 2
#         y = str(s)+ y
#         x //= 2
#     return y
# print(trans(6))

#Task 7
# def compare(x,y):
#     if x > y:
#         return'1'
#     elif x < y:
#         return'-1'
#     else:
#         return '0'

# print(compare(1,2))       

#Task 8
# a = 'Natural, Gay, Chmo, Pidr'
# def count_words(s):
#    s = a.count(' ') + 1 
#    return s
# print(count_words(a)) 

#Task 9
# a = 'Natural Gay Chmo Pidr'
# def divide_words(x):
#     for i in (x):
#         s = list(x.split(' '))
#         return s

# print(divide_words(a))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Task 1
# def reverse_text(result):
#     s = int(len(result) // 2)
#     result[:s] = result[:s][::-1]
#     result[s:] = result[s:][::-1]
#     return result

# print(reverse_text(['gay', 'getero', 'bisexual', 'transgender']))

#Task 3
# def fibonachi():
#     x1, x2 = 1, 1
#     lst = []
#     for i in range(10):
#         lst.append(x1)
#         x1, x2 = x2, x1 + x2
#     return lst              

# print(fibonachi())  

#Task 4
# def join2(x,y):
#    result = x - y
#    return result

# def delete2(x,y):
#    result = x + y
#    return result

# def both(x,y):
#    return join2(x,y), delete2(x,y)

# print(both(1,1))

#Task 5
# def create_file(name):
#     name = input()
#     my_file = open(name, 'w')
#     my_file.close

# create_file()

#Task 6
# import random
# def gen_number():
#     number = '0444'
#     nums = '145790'
#     for i in range(6):
#         number += random.choice(nums)
#     return number

# print(gen_number())

# Chat >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Task #1
# def factorial(n):
#     for i in range(n -1, 0, -1):
#         n = n * i
#     return n

# print(factorial(5))    

#Task 2
# def simple(n):
#     if n % n == 0 and n != 0 and n % 2 == 0:
#         return True
#     else:
#         return False
    
# print(simple(3))    

#Task 3
# n = int(input())
# def no_boring_zeros(n):
#     while True:
#         if n == 0:
#             return n 
#         elif n % 10 == 0:
#           n =  n // 10  
#         else:
#             return n

# print(no_boring_zeros(n))   
# sentence = "Hey fellow warriors"
# def spin_words(sentence):
#     full = ''
#     for i in sentence.split( ):
#         if len(i) > 5:
#             full += ' ' + i[::-1]
#         else:
#             full += i
#     return full

# print(spin_words(sentence))

