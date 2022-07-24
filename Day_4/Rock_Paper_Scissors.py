import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose=[rock,paper,scissors]



your_choose=int(input("What do you want to choose? Type 0 for Rock , 1 for Paper and 2 for Scissors ?\n"))

if your_choose<0 or your_choose>=3:
    print("invalid Number , You Lose!!")
else:
    print(choose[your_choose])
    Computer_choose = random.randint(0, 2)
    print("Computer Choice :" + choose[Computer_choose])
    if your_choose == Computer_choose:
        print("It's a draw")
    elif your_choose == 0:
        if Computer_choose == 1:
            print("YOU LOSE !!!!")
        else:
            print("YOU WIIIN !!!!!!!!!")
    elif your_choose == 1:
        if Computer_choose == 0:
            print("YOU WIIIN !!!!!!!!!")
        else:
            print("YOU LOSE !!!!")
    else:
        if Computer_choose == 0:
            print("YOU LOSE !!!!")
        else:
            print("YOU WIIIN !!!!!!!!!")

