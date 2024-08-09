def password(length):
    import random

    print("welcome to the automatic password generator")

    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"

    Password = []
    for i in range(1,length+1):
        Password.append(random.choice(chars))

    return ''.join(Password)

