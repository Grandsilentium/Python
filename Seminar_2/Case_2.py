# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = abs(float(input('Введите вещественное число: ')))
sum=0
for i in str(number):
    if i != '.':
        sum += int(i)
print(sum)

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('введите число: '))
mult = 1
for i in range(2, number+1):
    print(mult, end =",")
    mult=mult*i
print(mult)


# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#*Пример:*
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

print('Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')
n = int(input('Введите число N:-> '))
seq = dict()
seq_sum = 0
for i in range(1, n+1):
    seq[i] = round((1+1/i)**i, 2)
print(f'Для N={n} {seq}')
print(f'Сумма {sum(seq.values())}')

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

num = int(input("Ведите число: "))
my_list = []
for i in range(num):
    my_list.append(random.randint(-num, num))
print(my_list)

path = 'file.txt'
data = open(path, 'w')
data.write('2\n')
data.write('4\n')
data.close()

path = 'file.txt'
data = open(path, 'r')
mult = 1
for line in data:
    mult *= my_list[int(line)]
print(mult)

# 5 Реализуйте алгоритм перемешивания списка.

import random

def list_shuffle(my_list: list):
    shuffled_list = []
    temp_list = my_list.copy()

    for _ in range(len(my_list)):
        position = random.randint(0, len(temp_list) - 1)
        shuffled_list.append(temp_list.pop(position))
    return shuffled_list

print(list_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
