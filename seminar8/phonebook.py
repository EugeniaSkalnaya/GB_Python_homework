def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('newphonebook.csv')
    while (choice != 7):
        if choice == 1: #works
            print_result(phone_book)
        elif choice == 2: #works
            surname = get_search_surname()
            print(find_by_surname(phone_book, surname))
        elif choice == 3: #works
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4: #works
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('newphonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)  
        elif choice == 6:
            surname = get_search_surname()
            newres = del_by_surname(phone_book, surname)
            write_csv('newphonebook.csv', newres)
            phone_book = newres
            print("Абонент удален ")
                 
        choice = show_menu()  
        
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента по фамилии\n"
          "7. Закончить работу")
    return int(input())

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Комментарий"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

#works        
def print_result(data: list) -> None:
    print('\nФамилия---Имя---Телефон--Описание:\n')
    with open('newphonebook.csv', 'r', encoding='utf-8') as info:
        print(info.read())

#works
def get_search_surname():
    return input("\nВведите фамилию для поиска: ")

#works    
def find_by_surname(phone_book: list, surname: str) -> str:
    res = []
    for line in phone_book:
        if surname == line['Фамилия']:
            res.append(line['Телефон'])
            res.append(line['Имя'])
            res.append(line['Комментарий'])
    if (len(res) == 0):
        return f'В справочнике нет абонентов с фамилией {surname}'
    else:
        return f'Информация по абоненту с фамилией {surname}: ' + ', '.join(res)
#works
def get_search_number():
    return input('\nВведите номер телефона: ')

#works
def find_by_number(phone_book, phone) -> str:
    res = []
    for line in phone_book:
        if phone == line['Телефон']:
            res.append(line['Фамилия'])
            res.append(line['Имя'])
            res.append(line['Комментарий'])
    if (len(res) == 0):
        return f'В справочнике нет абонентов с телефоном {phone}'
    else:
        return f'Информация по абоненту с телефоном {phone}: ' + ', '.join(res)
#works
def get_new_user()-> list:
    print('Введите данные нового абонента: ')
    new_user = []
    new_user.append(input('Фамилия: '))
    new_user.append(input('Имя: '))
    new_user.append(input('Телефон: '))
    new_user.append(input('Комментарий: '))
    return new_user

#works
def add_user(phone_book, user_data):
    phone_book.append({'Фамилия': f'{user_data[0]}', 'Имя': f'{user_data[1]}',
                      'Телефон': f'{user_data[2]}', 'Комментарий': f'{user_data[3]}'})

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def get_file_name():
     return input('Введите имя файла: ') + '.txt'


def write_txt(file_name, phone_book):
    with open(file_name, 'w', encoding='utf-8') as fout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def del_by_surname(phone_book, surname) -> list:
    res = []
    for line in phone_book:
        if surname != line['Фамилия']:
            res.append(line)
    return res


def del_by_number(phone_book, number) -> list:
    res = []
    for line in phone_book:
        if number != line['Телефон']:
            res.append(line)
    return res

work_with_phonebook()
