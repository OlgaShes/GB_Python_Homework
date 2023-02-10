# Задача 26.
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(num, p):
    if p == 1:
        return num
    return num * power(num, p - 1)
    
a, b = int(input('A = ')), int(input('B = '))

print(f'{a} в степени {b} равно {power(a, b)}')
