# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    password = [];
    string_lenght = random.randint(8,16)
    for i in range(string_lenght):
        if i % 4 == 0:
            char = chr(random.randint(97,122))
        elif i % 4 == 1:
            char = chr(random.randint(65,90))
        elif i % 4 == 2:
            char = chr(random.randint(48,57))
        elif i % 4 == 3:
            char = SYMBOLS[random.randint(0,27)]
        password.append(char)

    random.shuffle(password)
    
    return ''.join(password)

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
