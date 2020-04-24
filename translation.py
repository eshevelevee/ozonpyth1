print("Введите слова и их переводы, а я потом вас потестирую!")

dictionary = {}

# Цикл для заполнения словаря
while True:
    key = input("Введите слово на английском или stop: ")
    if key == "stop":
        break
    value = input("Введите перевод или stop: ")
    if value == "stop":
        break
