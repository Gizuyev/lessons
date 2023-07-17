#Task 1
# lang1 = 'Rust'
# languages = ['Rust','go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if lang1 in languages:
#         print('This language is in list')
#         break
#     else:
#         print('')

#Task 2
# for i in range(1, 11):
#     print(i)

#Task 3
# numbers = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         numbers.append(i)
# print(numbers)

#Task 4 
# for i in range(1, 101):
#     s = i * (i + 1)/ 2
# print((s))

#Task 5 
# num = int(input())
# for i in range(1, 11):
#     s = num * i
#     print(num, 'x', i, '=', s)

#Task 6 
# for i in range(1, 6):
#     s = i * i + 1
# print(s) 

#Task 7
# for i in 'Hello World':
#     if i == ' ':
#         continue
#     print(i)

#Task 8 
# s = [1, 2, 3, 4, 5]
# for i in s:
#     x = i + i + i
# print(x)    

#Task 9 
# s = [1, 2, 2, 3, 4, 4, 5]
# s2 = []
# for i in s:
#     if i in s2:
#         continue
#     else:
#         s2.append(i)
# print(s2)

#Task 10
# for i in range(10, 0, -1):
#     print(i)        

#Task 11
# s = []
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         s.append(i)
# print(s)

#Task 12
# s = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in s:
#     if i == "php":
#         break
#     print(i)        

#Task 13
# num = int(input())
# for i in range(5):
#     s = num * num
# print(s)

#Task 14
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     print(languages.index(i), i)

#Task 15
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# names2 = []
# for i in names:
#     if names.index(i) % 2 == 0:
#         names2.append(i)
# print(names2)        

#Task 16
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# for i in range (0, 13, 2):

#Task 17
# num = int(input())
# s = str(num)
# if len(s) == 3:
#     print('Число трехзначное')
# else:
#     ('Число не является трехзначным')
# if num > 0:
#     print('Число положительное')
#     if num % 2 == 0:
#         print('Число четное')
#     else:
#         print('Число нечетное')
# if num % 31 == 0:
#     print('Число делится без остатка на 31')
# else:
#     print('Число не делится на 31 без остатка')
# if num > 100 and num % 17 == 0 or num > 150 and num == 13 ** 2:
#     print(num)

#Task 18
# list1 = []
# list2 = []
# for i in range(-100, 100):
#     if i % 13 == 0 and i > 0:
#         num = i ** 2
#         list1.append(num)
# for i in range(-100, 100, 7):
#     if i % 2 != 0:
#         list2.append(i)
# print(list1)
# print(list2)             

a = abs(float(input()))
b = abs(float(input()))
c = abs(float(input())) 
d = abs(float(input())) 
e = abs(float(input()))
print(a + b + c + d + e)
