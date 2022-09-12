import pandas as pd
nato=pd.read_csv("nato_phonetic_alphabet.csv")


nato_dict={str(row.letter):str(row.code) for (index,row) in nato.iterrows()}

user_word=input("Enter A word : ")

result=[nato_dict[letter.upper()] for letter in user_word]
print(result)