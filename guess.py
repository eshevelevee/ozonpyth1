import random
print('''Добро пожаловать в Великую Игру "Угадай число"!!!''')
print('''Выберите уровень: ''')
print('1. Легкий', '2. Средний', '3. Сложный', sep='\n')
level = int(input("Выберите уровень:"))
number = random.randint(1, 50)
if level == 1:
    trys = 12
elif level == 2:
    trys = 9
else:
    trys = 6
counter = 0
while counter < trys:
    answer = int(input("Попробуйте угадать число (введите целое число от 1 до 50): "))
    if answer == number:
        print("О Боги, вы победили с " + str(counter + 1) + " попытки")
        break
    elif answer < number:
        print("Нет, я загадал побольше. У вас осталось " + str(trys - counter - 1) + " попыток")
    elif answer > number:
        print("Нет, я загадал поменьше. У вас осталось " + str(trys - counter - 1) + " попыток")
    counter += 1
else:
    print("Извините, вы не угадали!")
