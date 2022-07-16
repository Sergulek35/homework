# МОДУЛЬ 6

print('Здравствуйте, начнём викторину!!!')
game = 'да'
over = 'нет'
question = ''
while question != over:
    print('-' * 50)
    correct_answer = 0
    wrong_answer = 0
    gagarin = int(input('В каком году Ю.Гагарин совершил свой первый полёт? -  '))  # 1961
    while gagarin != 1961:
        if True:
            wrong_answer += 1
        print('Неверно!!')
        gagarin = int(input('  Попробуйте ещё раз:  '))
    correct_answer += 1
    print('Ответ правильный!\n Идём дальше...')

    pushkin = int(input('Укажите год рождения А.С.Пушкина -  '))  # 1799
    while pushkin != 1799:
        if True:
            wrong_answer += 1
        print('Неверно!!')
        pushkin = int(input('  Попробуйте ещё -  '))
    correct_answer += 1
    print('Правильно!\nПродолжаем...')

    pugacheva = int(input('В каком году родилась Пугачёва А.Б ? -  '))  # 1949
    while pugacheva != 1949:
        if True:
            wrong_answer += 1
        print('Неверно!!')
        pugacheva = int(input('  Попробуйте ещё -  '))
    correct_answer += 1
    print('Верно!\nДалее...')

    einstein = int(input('Укажите год рождения А.Эйнштейна: -  '))  # 1879
    while einstein != 1879:
        if True:
            wrong_answer += 1
        print('Неверно!!')
        einstein = int(input('  Попробуйте ещё -  '))
    correct_answer += 1
    print('Хорошо!\nИ последний вопрос...')

    michael = int(input('Год рождения Майкла Джексона -  '))  # 1958
    while michael != 1958:
        if True:
            wrong_answer += 1
        print('Неверно!!')
        michael = int(input('  Давайте ещё -  '))
    correct_answer += 1

    total_answers = correct_answer + wrong_answer
    correct_procen = correct_answer * 100 / total_answers
    answer_procen = wrong_answer * 100 / total_answers

    print('-' * 50)
    print('Вы молодец!!')
    print('Верно:', correct_answer, '\nОшибки:', wrong_answer)
    print('Процент правильных ответов - ', int(correct_procen), '%')
    print('Процент неверных ответов - ', int(answer_procen), '%')

    print('*' * 50)

    question = input('Хотите начать сначала? ')
    if question == game:
        print('Продолжаем!')
    elif question == over:
        print('Всего Вам доброго!')
    else:
        print('Не правильный ввод\nПрограмма закрыта!')
        break
