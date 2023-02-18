def start():
    print('''\t Список классов:
    \t 1. 11a
    \t 2. 11b
    \t 3. 11c
    ''')
    start = int(input("Выберите класс: "))
    return start

def choose_lesson():
    print('''\t Список предметов:
    \t 1. Алгебра
    \t 2. Русский язык
    \t 3. Обществознание
    ''')
    lesson = int(input('Выберете предмет: '))
    return lesson

def print_classes(lesson, my_dict):
    match lesson:
        case 1:
            for keys, value in my_dict.items():
                print(f"\t{keys}: {value['Алгебра']}")
        case 2:
            for keys, value in my_dict.items():
                print(f"\t{keys}: {value['Русский язык']}")
        case 3:
            for keys, value in my_dict.items():
                print(f"\t{keys}: {value['Обществознание']}")

def who_go(my_dict):
    i = 0
    new_dict = {}
    print('\t\tCписок учеников: ')
    for keys in my_dict:
        i += 1 
        print(f'\t{i}. {keys}')
        new_dict[i] = keys   
    puple = int(input('Выберите того, кто пойдет к доске: '))

    if puple in new_dict:
        return new_dict[puple]

# def grade(num, my_dict):
#         for keys in my_dict:
#             if keys == num:
#                 print('да')  
