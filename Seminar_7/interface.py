from os.path import exists
from scv_creating import creating
from file_writing import writing_scv, writing_txt, get_info
from export import from_file


def view():
    print(from_file('Phonebook.txt'))


def record_info():
    info = get_info()
    writing_scv(info)
    writing_txt(info)


def choice():
    flag = input(
        'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    while (flag.lower() == 'да'):
        path = 'Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Введите \'да\', если хотите записать новые данные, и любой другой символ, если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'да':
            record_info()
        else:
            view()
        flag = input(
            'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    print('Программа завершена.')
