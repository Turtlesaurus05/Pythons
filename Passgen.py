import random

chars = "abcdefghijklmnopqrstuvwxyz"
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numb = "13456789"
spec = "!?=$€)({[}]@"

while 1:
    password_len = int(input("How long would you want your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0, password_count):
     password = ""

    for x in range(0, password_len):
        password_char = random.choice(chars + CHARS + numb + spec)
        password = password + password_char
    print("Your password is :", password)
    breakpoint()

