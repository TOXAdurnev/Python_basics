a = int(input('Введите челое положительное число : '))
x = a % 10
a = a // 10
while a > 0:
    if a % 10 > x:
        x = a % 10
    a = a//10
print(x)