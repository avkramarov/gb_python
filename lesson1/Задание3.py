# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input("Введите число >>>")
number1 = int(user_number)
number2 = int(user_number + user_number)
number3 = int(user_number + user_number + user_number)
print(number1 + number2 + number3)
