import random
bullets = [0 for i in range(random.randint(0,100))]
bullets[random.randint(0, len(bullets)-1)] = 1

a = int(input("Хочешь сыграть в игру? Если да, то напиши 1б а если нет, то 0: "))

while a == 1:
    if random.choice(bullets) == 1:
        print("Ты проиграл! Хочешь сыграть еще раз?")
    else:
        print("Ты выиграл!")
    a = int(input("Хочешь сыграть в игру? Если да, то напиши 1б а если нет, то 0: "))



