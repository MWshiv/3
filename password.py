import random
def password():
    a = ""
    for i in range(random.randint(7, 10)):
        a += chr(random.randint(33,126))
    return a
print(password())
