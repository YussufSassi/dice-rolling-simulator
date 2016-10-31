from random import randint

while True:
    number = randint (1,6)
    print(number)
    option = input("Do you want to the roll the dice again?(yes/no)? ")
    yes = ["yes", "Yes", "y", "Y", "ja", "si","oui", "evet", "po","da"]
    if option in yes:
        continue
    else:
        print("Quitting now...")
        break
