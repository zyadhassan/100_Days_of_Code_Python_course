# Treasure Island Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____''')

print(" Welcome To Treasure island \n")
print("Your Mission to find the Treasure\n")

if str(input("you are at a cross road! where will you go? Type 'Left' or 'Right'?\n")) =='Left' :
    if str(input("You have come to a lake , there is an island in the middle of the lake will you swim or wait a boat? Type 'Swim' or 'Wait' ?\n"))=='Wait' :
        door=input("You Find Three doors red,blue and yellow which one will you choose? Type 'r' or 'b' or 'y' ?? \n")
        if door=='r':
            print("Burned by fire \n GAME OVER!!!!!!")
        elif door=='b':
            print ("Eaten by Beats \n GAME OVER!!!!!!")
        elif door=='y':
            print("YOU WIIIIIIINNNNNN !!!!!!!!!!!")
        else:
            print("GAMEEEEE OVEEEEER!!")
    else:
        print("Attacted by troat \n GAME OVER!!!!")
else:
    print('Fall into a hall GAME OVER!!!!')




