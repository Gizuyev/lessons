#Task 1
# dates_of_birth = {3,10,11,7,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)

#Task 2
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_1.intersection(farm_2))

#Task 3
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_2.difference(farm_1))

#Task 4
# supernaturaly = {'Conor', 'Las Veags', 'Alex Gordon', 'Danny Phantom', 'Gay'}
# supernaturaly.add('Alkash')
# print(supernaturaly.pop())

#Task 5
# menu = {'lagman': 120,
#         'plov': 120,
#         'borsh': 100,
# }
# menu['besh_barmak'] = 130
# print(menu)
# menu['besh_barmak'] = 135
# print(menu)
# menu.pop('borsh')
# print(menu)

#Task 6
# menu = {'lagman': 120,
#          'plov': 120,
#          'borsh': 100,
# }
# menu['drinks'] = ['Coca - Cola', 'Sprite', 'Fanta']
# print(menu)

#Task 7
# set1 = {'add()', 'remove()', 'clear()', 'update()','difference()', 'discard()', 'intersection()', 'pop()'}
# set2 = {'clear()', 'get()', 'keys()', 'valuses', 'items()', 'update()'}
# print(set1.intersection(set2))

#Task 8
# d = {}
# for i in range(3):
#     a = input('Name: ')
#     b = input('Password: ')
#     d[str(a)] = b
# print(d)

#Task 9
# workers = {'Ibragim': 'Senior Developer',
#            'Bektur': 'Junior Developer',
#             'Ruslan': 'Stazher',
# }
# for key, value in workers.items():
#     print(f'Здрвствуйте {key}! Прекрасная работа {value}')

#Task 10
# a = set()
# for i in range(10):
#     num = int(input())
#     a.add(num)
# print(tuple(a))    

#Task 11
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
# 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# print()
# a = set(south_american_countries)
# print(a)

#Task 12
# suitcase = []
# for i in range(5):
#     suitcase.append(input())
# suitcase.remove(suitcase[-1])    
# print(suitcase)

#Task 13
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_2.intersection(farm_1)
# print(farm_3)

# #Task 14
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_2.difference(farm_1)
# print(farm_3)

#Task 15
# house = {
#     "гостиная": {
#         "диван": 10,
#         "стол": 5,
#         "телевизор": 3,
#         "кресло": 7
#     },
#     "кухня": {
#         "стол": 6,
#         "стул": 3,
#         "холодильник": 4,
#         "плита": 5
#     },
#     "спальня": {
#         "кровать": 12,
#         "шкаф": 8,
#         "тумбочка": 2,
#         "комод": 6
#     },
#     "ванная": {
#         "ванна": 10,
#         "раковина": 4,
#         "туалет": 3,
#         "зеркало": 2
#     }
# }
# count = 0
# for i in house:
#     for j in house[i]:
#         print(j, house[i][j])
#         count += house[i][j]
# print(count)
