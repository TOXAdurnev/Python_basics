a = int(input('Укажите сколько километров стоставил результат спортсмена в первый день:  '))
b = int(input('Укажите сколько километров стоставил общий результат спортсмена:  '))
day = 1
while (b - a) > 0:
    print("%s-й день: %.2f" % (day, a))
    a = a+(a * 0.1)
    day = day+1
print("%s-й день: %.2f" % (day, a))

print("Ответ: на %s-й день: спортсмен достиг результата - не менее %s км" % (day, b))