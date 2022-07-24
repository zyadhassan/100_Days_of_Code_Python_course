import art
import random
print(art.logo)
print("Welcome to Number Gussing Game")
print("i am thinking of a number between 1 and 100")
num=random.randint(1,100)
#print(num)
diffuclty=input("Choose a difficulty. Type 'easy' or 'hard':")
if diffuclty=='easy':
    attempts=10
elif diffuclty=='hard':
    attempts=5
else:
    diffuclty=input("invalid lever , Type 'easy' or 'hard': ")
    if diffuclty == 'easy':
        attempts = 10
    elif diffuclty == 'hard':
        attempts = 5

win=False

while attempts>0 and not win:
    print(f"You have {attempts} attempts remaning to guess the number")
    guess=int(input("what you guess? :"))
    if guess<num:
        print("too low")
        attempts-=1
    elif guess>num:
        print("too high")
        attempts-=1
    elif guess==num:
        win=True

if attempts==0:
    print("You finishe your attempts ")
    print("You Lose!")
elif win :
    print("You Win!!")