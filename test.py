
b = input("Введите имя ")
a = int(input("Введите номер из списка "))
names = ['egor', 'ivan', 'petr', b]
names.reverse()
print(names[a].title())
print(names)
counter = 0
# while counter != len(names):
#     print(names[counter].title())
#     counter += 1

for i in names:
    print(i)