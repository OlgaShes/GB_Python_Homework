# Задача 2:
# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
sum_digits = 0

if 99 < number < 1000:
    while number != 0:
        sum_digits += number % 10
        number //= 10
    print(f'Сумма цифр числа = {sum_digits}')
else:
    print('Необходимо ввести трехзначное число.')
