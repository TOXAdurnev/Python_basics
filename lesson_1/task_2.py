second = int(input('Введите кол-во секунд: '))

second = second % (24 * 3600)

hour = second // 3600

minutes = second // 60

seconds = second // 60

print("%02d:%02d:%02d" % (hour, minutes, seconds))