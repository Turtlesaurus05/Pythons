import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!?=$€"

while 1:
    password_len = int(input("How long would you want your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0, password_count):
     password = ""
     for x in range(0, password_len):
            password_char = random.choice(chars)
            password      = password + password_char
            print("Your password is : ",password)

