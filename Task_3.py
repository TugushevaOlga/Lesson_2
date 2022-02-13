# решение через list
month = input('Введите месяц в виде целого числа от 1 до 12 :')
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
while month.isdigit() and 0 < int(month) <= 12:

    if month in winter:
        print('Зима')
    elif month in spring:
        print('Весна')
    elif month in summer:
        print('Лето')
    elif month in autumn:
        print('Осень')
        break
else:
    print('Неверно введен номер месяца')

# решение через dict
number = int(input('Enter month number: '))
season_dict = {12: 'Winter', 1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
               6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}

print(season_dict.get(number))

# изящное решение из разбора
while True:
    user_month = input('Введите номер месяца: ')
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Узнаём сезон через список:  {season_1[int(user_month) // 3]}'
              f'\nУзнаём сезон через словарь: {season_2[int(user_month) // 3]}')
        break
    else:
        print('Неправильно введен номер месяца')
