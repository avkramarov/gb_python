# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды 
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_number = int(input("Введите количество секунд >>>"))
clock = user_number // 3600
minute = (user_number % 3600) // 60
if (minute < 10):
    minute = "0" + str(minute)
sek = user_number % 60
if (sek < 10):
    sek = "0" + str(sek)
print("{}" ":" "{}" ":" "{}".format(clock, minute, sek))
