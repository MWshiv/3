import random
a = random.randint(1, 10)
while True:
    b = int(input("Угадайте число от 1 до 10: "))
    if a != b:
        print("Ваше число больше загаданного!") if b > a else print("Ваше число меньше загаданного!")
    else:
        print("Победа!!!!!")
        break
