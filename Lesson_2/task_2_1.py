#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


super_list = [5, 1.2, 'Hello world', ['a', '2'], ('b', '3'), {'city': 'Moscow', 'country': 'Russia'}]
for i in super_list:
    print(f'{i} is {type(i)}')


