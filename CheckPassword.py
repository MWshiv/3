def CheckPassword(a):
    return len(a) >= 8 and a!=a.lower() and a!=a.upper()
print(CheckPassword(input("Введите пароль ")))
