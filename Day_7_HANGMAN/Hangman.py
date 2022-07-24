import random
import hangman_art
import hangman_words

print(hangman_art.logo)
choosen_word=random.choice(hangman_words.word_list)



stri=[]
for i in choosen_word:
    stri.append('_')


flag=False
lives=6
s=-1
wrong=[]
while( not ( "_" not in stri)) and lives>=0 :
    guess_letter = str(input("Guess a letter :")).lower()
    for i in range(0,len(choosen_word)):
        if choosen_word[i]==guess_letter:
            stri[i]=choosen_word[i]
            flag=True
    if flag:
        print(f"you guessed letter {guess_letter} :")

        print(f"{' '.join(stri)}")
        # to print list like string use join function " string.join(list) " while string will be printed between elements
        flag=False
    else:
        if(guess_letter in wrong):
            print(f"you guessed {guess_letter} before, wrong guess")

        else:
            print(f"you guessed {guess_letter}, wrong guess ---lives remain {lives}")
            lives-=1
            print(hangman_art.stages[s])
            s-=1
            wrong.append(guess_letter)


if( "_" not in stri):
    print("YOU WON")

else: print("YOU LOSE")