FILE_PATH = 'phone_book.txt'

def print_all_contacts():
    print('\nВсе контакты:')
    with open(FILE_PATH, 'r', encoding='utf8') as data:
        for line in data:
            print(line.strip())

def find_contact(name: str):
    not_found = True
    with open(FILE_PATH, 'r', encoding='utf8') as data:
        for line in data:
            if name.lower() in line.lower():
                not_found = False
                print(line.strip())
    if not_found:
        print('Такой контакт не найден')

def add_contact(new_contact: str):
    with open(FILE_PATH, 'a', encoding='utf8') as data:
        data.write('\n' + new_contact)
    print('Контакт записан')

def change_book(old_contact: str):
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        book = file.readlines()
    not_found = True
    for i in range(len(book)):
        if old_contact.lower() in book[i].lower():
            print(f'Найден контакт -> {book[i].strip()}\nХотите его изменить? '
                  '(1 - изменить, 2 - удалить, 3 - искать другой контакт)')
            mode = input()
            if mode == '1':
                book = change_contact(book, i)                
                not_found = False
                break
            elif mode == '2':
                book = delete_contact(book, i)                
                not_found = False
                break
    if not_found:
        print('Контакт не найден, изменения не прошли')
    else:
        with open(FILE_PATH, 'w', encoding='utf8') as file:
            book = file.writelines(book)
    
def change_contact(contact_list: list, index: int) -> list:
        operation = input('Что хотите изменить? 1 - имя, 2 - фамилию, 3 - номер телефона \n')
        while operation not in ('1', '2', '3'):
            print('Некорректный ввод. \nВведите 1 для изменения имени, 2 - фамилии, 3 - номера телефона')
            operation = input().strip()
        contact = contact_list[index].split()
        new_value = input('Введите новое значение: ').strip()
        contact[int(operation) - 1] = new_value
        contact_list[index] = ' '.join(contact).title() + '\n'
        print('Контакт изменен, новый контакт: ')
        print(contact_list[index].strip())
        return contact_list
        
def delete_contact(contact_list: list, index: int) -> list:
    contact_list.pop(index)
    print('Контакт удален')
    return contact_list

