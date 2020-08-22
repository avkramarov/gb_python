# Пользователь вводит целое положительное число. 
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_number = int(input("Введите число >>>"))
max = 0
while user_number > 0:
    a = user_number % 10
    user_number //= 10
    if a > max:
        max = a
print(max)
