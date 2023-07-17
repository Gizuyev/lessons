cities = []
while True:
    choice = input(
    'Выберите команду: \n'
    '1. Добавить новый город \n'
    '2. Отобразить список городов \n'
    '3. Заменить город \n'
    '4. Удалить город \n'
    '5. Выход \n')
    if choice == '5':
        print('Сеанс завершен!!!!')
        break
    elif choice == '1':
        city_name = input('Ведите название города: ')
        if city_name in ', ,  ,   ,    ,     ' or city_name.isdigit():
            print('Город не может состоять из чисел, символов и пробелов !!!')
        elif city_name in cities:
            print('Такой город уже есть !!!')    
        else:
            cities.append(city_name)
            print('Список городов: ', cities)
    elif choice == '2':
        print()
        print(cities)
    elif choice == '4':
        print(cities)
        print('Введите нумерацию города который хотите удалить')
        deleted_city = int(input('Первый город под номером "0", и по возрастанию: 0,1,2... '))
        print(f'Город {cities[deleted_city]} был удален(((')
        cities.pop(deleted_city)
    elif choice == '3':
        print(cities)
        print('Введите нумерацию города который хотите заменить')
        changed_city = int(input('Первый город под номером "0", и по возрастанию: 0,1,2...'))
        added_city = input('Введите навзвание города которым хотите заменить: ')
        print(f'Город {cities[changed_city]} был заменен на {added_city}') 
        cities[changed_city] = added_city 
         







