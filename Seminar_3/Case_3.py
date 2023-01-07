# Урок 3. Данные, функции и модули в Python
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]

def sum_elem(my_list):
    sum = 0
    for i in range(len(my_list)):
        if (i % 2!=0):
            sum = sum + my_list[i]
    return sum

print(f'{"Ответ: "}{sum_elem(my_list)}')


# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil

def pair_multiplication(array):

    output_list = []
    for i in range(ceil(len(array)/2)):
        output_list.append(array[i] * array[-(i + 1)])
    return output_list

odd_list = [2, 3, 4, 5, 6]
even_list = [2, 3, 5, 6]

print(pair_multiplication(odd_list))
print(pair_multiplication(even_list))


# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
my_list=[1.1, 1.2, 3.1, 5, 10.01]

tails_list=[]

for i in range(len(my_list)):
    if my_list[i]%1 !=0:
        tails_list.append(round(my_list[i]-int(my_list[i]),2))

print(f'{my_list} => {max(tails_list) - min(tails_list)}')


# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def dec_to_bin(number): 
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    return result

number = int(input('Введите целое число: '))
print(dec_to_bin(number))



# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

def fibonacci (n):
    fibonacci_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fibonacci_list.append(x)
        fibonacci_list.insert(0, -x if i %2 else x)
    return fibonacci_list

number = int(input('введите число: '))
print(f'для k = {number} список будет выглядеть так: {fibonacci(number)}')