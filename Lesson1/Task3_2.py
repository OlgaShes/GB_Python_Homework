# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

ticket_number = [int(c) for c in input('Введите номер вашего билета: ')]

if len(ticket_number) != 6:
    print('Неверный номер билета')
elif sum(ticket_number[:3]) == sum(ticket_number[3:]):
    print('Поздравляю, билет счастливый!')
else:
    print('Увы, билет не является счастливым')