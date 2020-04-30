# Напишите функцию prime(number),
# в которую передается натуральное число, большее единицы.
# Функция должна возвращать строку «Простое число» в случае, если оно простое, и строку «Составное число» в противном случае.

def prime(number=int(input("Введите натуральное число больше 1: "))):
    if number % 2 == 0:
        print("Составное число")
        return 1
    delitel = 3
    while delitel * delitel <= number and number % delitel != 0:
        delitel += 1
    if delitel > number:
        print("Составное число")
    else:
        print("Простое число")


prime()
