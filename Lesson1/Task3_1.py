# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

def sum_of_digits(num):
    sum_digits = 0
    while num != 0:
        sum_digits += num % 10
        num //= 10
    return sum_digits

ticket = input('Введите номер вашего билета: ')

if ticket.isdigit() and len(ticket) == 6:
    ticket_number = int(ticket)
    first_digits = ticket_number // 1000
    last_digits = ticket_number % 1000
    if sum_of_digits(first_digits) == sum_of_digits(last_digits):
        print('Поздравляю, билет счастливый!')
    else:
        print('Увы, билет не является счастливым')
else:
    print('Неверный номер билета')
