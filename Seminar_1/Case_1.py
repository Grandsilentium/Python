# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

import math
number = int(input('Введите число: '))
if number == 6 or number == 7:
    print(f'{number} -> "Да"')
else:
    print(f'{number} -> "нет"')

# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('x y z result')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, not (x or y or z) ==
                  (not (x and not y and not z)))

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

point_x = int(input('введите x координату точки: '))
point_y = int(input('введите y координату точки: '))

if (point_x > 0 and point_y > 0):
    print('-> 1')
elif (point_x < 0 and point_y > 0):
    print('-> 2')
elif (point_x < 0 and point_y < 0):
    print('-> 3')
elif (point_x > 0 and point_y < 0):
    print('-> 4')

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти: '))

if (quarter_number == 1):
    print(" x [0: + ∞], y [0: + ∞]")
elif (quarter_number == 2):
    print(" x [0: - ∞], y [0: + ∞]")
elif (quarter_number == 3):
    print(" x [0: - ∞], y [0: - ∞]")
elif (quarter_number == 4):
    print(" x [0: + ∞], y [0: - ∞]")

# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

first_point_x = int(input('Введите координату точки A на оси x: '))
first_point_y = int(input('Введите координату точки A на оси y: '))
second_point_x = int(input('Введите координату точки B на оси x: '))
second_point_y = int(input('Введите координату точки B на оси y: '))

distance = round(math.sqrt((first_point_x-second_point_x)
                 * 2 + (first_point_y-second_point_y)*2), 2)
print(f'-> {distance}')