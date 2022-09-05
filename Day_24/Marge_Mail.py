
name_list=[]
letter=""

with open("./input/Letters/starting_letter.txt") as Letter:
    letter=Letter.read()

with open("./input/Names/invited_names.txt") as Names:
    name_list=Names.readlines()
    for name in name_list:
        name=name.strip()
for person in name_list:
    person=person.strip("\n")
    with open(f"./Output/ReadyToSend/Mail_to_{person }.txt",mode="w") as mail:
        mail.write(letter.replace("[name]",f"{person}"))