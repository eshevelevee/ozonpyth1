import random
a = int(input("Хочешь сыграть в игру? Если да, то напиши 1, а если нет, то 0: "))

while a == 1:
    bullets = [0 for i in range(random.randint(0, 100))]
    counter_bullets = 0
    number_bullets = random.randint(0, len(bullets) - 1)
    while number_bullets > 0:
        bullets[random.randint(0, len(bullets) - 1)] = 1
        number_bullets -= 1
        counter_bullets += 1
    if random.choice(bullets) == 1:
        print("Ты проиграл! У тебя было " + str(counter_bullets) + " из " + str(len(bullets)) + " шансов проиграть!. Хочешь сыграть еще раз?")
    else:
        print("Ты выиграл! У тебя было " + str(counter_bullets) + " из " + str(len(bullets)) + " шансов проиграть!. Хочешь сыграть еще раз?")
    a = int(input("Хочешь сыграть в игру? Если да, то напиши 1б а если нет, то 0: "))



