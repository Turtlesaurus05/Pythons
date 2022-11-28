import random #Imports a pip packet called Random

chars = "abcdefghijklmnopqrstuvwxyz"
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numb = "13456789"
spec = "!?=$€)({[}]@"

while 1:
    password_len = int(input("How long would you want your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0, password_count): #Asks how many chars you want and then randomizes from the 4
     password = ""

    for x in range(0, password_len):
        password_char = random.choice(chars + CHARS + numb + spec) #Chooses the random "marks
        password = password + password_char #Last step to make the password
    print("Your password is :", password) #Prints the password that was random generated
    breakpoint()

