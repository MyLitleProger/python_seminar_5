# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.

# рекурсивная функция возведения числа в целую степень
def degree_of_number(number, degree):
    if degree in [0]:
        return 1
    if degree in [1]:
        return number
    if degree > 1:
        return number * degree_of_number(number, degree - 1)
    if degree < 0:
        return 1 / (number * degree_of_number(number, -degree - 1))


# ввод первого числа с проверкой на число
while True:
    try:
        number_1 = float(input('Введите возводимое число: '))
        break
    except ValueError:
        print('Введите любое число!')

# ввод второго числа с проверкой на целое
while True:
    try:
        number_2 = int(input('Введите степень числа: '))
        break
    except ValueError:
        print('Введите любое ЦЕЛОЕ число!')

# вывод
print(f'Число {number_1} в степени {number_2} = {degree_of_number(number_1, number_2)}')
