import random
a = random.randint(1, 10)
while a != (b := int(input("Угадайте число от 1 до 10: "))):
    print("Ваше число больше загаданного!") if b > a else print("Ваше число меньше загаданного!")
print("Победа!!!!!")
