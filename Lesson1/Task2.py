# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

cranes_total = int(input('Сколько всего сделали журавликов? '))

if cranes_total < 0:
    print('Количество журавликов не может быть отрицательным')
elif cranes_total % 6 != 0:
    print('Такое количество не могло получиться по условиям задачи')
else:
    cranes_boys = cranes_total // 6
    cranes_katia = cranes_boys * 4
    print(
        f'Петя сделал {cranes_boys} журавликов, Катя {cranes_katia} журавликов, Сережа {cranes_boys} журавликов')
