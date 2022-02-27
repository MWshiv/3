a = input("Введите пароль ")
def CheckPassword(a):
    if len(a) >= 8 and a!=a.lower() and a!=a.upper():
        return True
    return False
print(CheckPassword(a))
