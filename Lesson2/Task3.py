# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('Введите число: '))

index = 0
power_of_2 = 1

while power_of_2 <= n:
    print(power_of_2, end=' ')
    index += 1
    power_of_2 = 2 ** index
    

