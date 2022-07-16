 # МОДУЛЬ 5 условные операторы и цикл while:

date = int(input("введите год рождения Пушкина А.С. - "))
year = 1799
while date != year:
    print('Неверный год!!')
    date = int(input('попробуйте ещё раз: '))
if date == year:
    day = float(input("введите день рождения Пушкина А.С.(число.месяц) - "))
while day != 06.06:
    print('Неверный день рождения!!')
    day = float(input('введите снова: '))

print('Всё верно!!!')
