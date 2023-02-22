import operations as op

def get_help():
    instructions = 'Для работы со справочником используйте команды:\n'\
                         '1 - печать всей телефонной книги\n'\
                         '2 - поиск контакта\n'\
                         '3 - запись нового контакта\n'\
                         '4 - изменение контакта\n'\
                         '5 - для выхода из программы'
    print(instructions)

def main_menu():
    command = ''
    while command != '5':
        command = input('\nВведите команду: ')
        if command == '1':
            op.print_all_contacts()
        elif command == '2':
            name = input('Введите искомое имя: ')
            op.find_contact(name)
        elif command == '3':
            first_name = input('Введите имя нового контакта: ')
            second_name = input('Введите фамилию нового контакта: ')
            phone_number = input('Введите номер нового контакта: ')
            op.add_contact(f'{first_name} {second_name} {phone_number}')
        elif command == '4':
            old_name = input('Какой контакт хотите поменять? ')
            op.change_book(old_name)   
        elif command == '5':
            print('Спасибо за использование нашей телефонной книжки! До свидания!')
        else:
            get_help()
