import random

print("Введите слова и их переводы, а я потом вас потестирую!")

dictionary = {}

# Цикл для заполнения словаря
while True:
    key = input("Введите слово на английском или stop: ").lower()
    if key == "stop":
        break
    value = input("Введите перевод или stop: ").lower()
    if value == "stop":
        break
    dictionary[key] = value
scores, errors = 0, 0
print("Let's go!")
l = list(dictionary.items())
random.shuffle(l)
dictionary = dict(l)
for k, v in dictionary.items():
    translation = input('Введите перевод слова ' + k + ":")
    if translation == v:
        scores +=1
        print("OK!")
    else:
        errors +=1
        print("Not ok!")

