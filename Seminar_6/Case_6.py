# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1 Пример использования lambda

Возвести в степень n число m.

n = int(input())
m = int(input())

pow = lambda x, y: x**y

print(pow(n,m))



# 2 Пример использования filter

Задайте список из нескольких чисел. Напишите программу, которая оставит в списке только нечетные элементы.


my_list = [2, 3, 5, 9, 3]
print(my_list)
select = lambda x : x % 2 != 0


print(list(filter(select, my_list)))

# 3 Пример использования map

Задайте список из натуральных чисел, выведите куб нечетных элементов списка.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
select= lambda x: x%2 !=0
pow = lambda x: x**3

filtresd_list = list(filter(select,my_list))
print(filtresd_list)
new_list = list(map(pow, list(filter(select,my_list))))
print(new_list)

# 4 Пример использования zip

Сопоставьте ФИО и город с помощью функции zip()

first_name = ["Михаил","Кирилл","Антон","Владимир","Игорь"]
last_name = ["Соколов","Петров","Сидоров","Михайлов","Фомин"]
fathers_name= ["Яковлевич","Олегович","Дмитриевич","Михайлович","Игоревич"]
city = ["Воронеж"," Москва","Тула","Самара","Екатеринбург"]

print(list(zip(last_name,first_name,fathers_name, city)))

# 5 Пример использования enumerate

Пронумеруйте города по списку начиная с 1

biggest_city = ["Москва", "Санкт - Петербург", "Новосибирск", "Екатеринбург", "Нижний Новгород", "Казань", "Челябинск", "Омск", "Самара", "Ростов - на - Дону"]

print(list(enumerate(biggest_city, start=1)))



# 6 Пример использования list comprehension

Задайте список до от1 до n+1

num = int(input())
my_list = [i for i in range(1, num+1)]

print(my_list)
