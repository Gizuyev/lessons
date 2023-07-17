# sentence = 'Hey fellow warriors'
# def spin_words(sentence):
#     full = []
#     for i in sentence.split( ):
#         if len(i) >= 5:
#             full.append(i[::-1])
#         else:
#             full.append(i)
#         string = ' '.join(full)    
#     return string
# print(spin_words(sentence))

# def people_with_age_drink(age):
#     if age <= 13:
#         return 'drink toddy'
#     elif age >= 14 and age <= 17:
#         return 'drink coke'
#     elif age >= 18 and age <= 19:
#         return 'drink beer'
#     elif age >= 20 and age <= 29:
#         return 'drink beer'
#     else:
#         return 'drink whisky'

# print(people_with_age_drink(21))

# def sum_mul(n, m):
#     if m < 0:
#         return 'INVALID'
#     elif n >= 0:
#         for i in range(n,m):
#             s = i + i +4
#         return s    
# print(sum_mul(2,9))            

# def is_palindrome(s):
#     if s[::-1] == s:
#         return True
#     else:
#         return False

# print()    


# total = 0
# for i in range(1, 6):
#     total += i
# print(total, end='*')