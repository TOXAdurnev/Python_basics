revenue = int(input('Сколько состовляет выручка вашей фирмы? Введите: '))
cost = int(input('Каовы издержки фирмы? Введите: '))
itog = revenue - cost
profitability = int((itog/revenue) * 100)
if itog > 0:
    print('Ваша фирма работает в прибыль. Прибыль составила :', itog)
    print(f"Рентабельность ровна: {profitability}% ")
    if itog > 0:
        Profit_per_Person = int(input('Введите кол-во сотрудников ващей фирмы: '))
        print(itog/Profit_per_Person )
    else:
        print()


elif itog == 0:
    print('Ваша фирма работает в прибыль, но и не работет в убыток.')
else:
    print('Ваша фирма работает в убыток. Потери  составляют :', itog)
