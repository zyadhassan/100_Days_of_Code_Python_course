logo = """
 _____________________
|  _________________  |
| | ZCalc        0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)






def add(n1,n2):
    """Takes two numbers and return the result of their sum"""
    return n1+n2


def sub(n1,n2):
    return n1-n2


def divide(n1,n2):
    return n1/n2


def multibly(n1,n2):
    return n1*n2
re_com=True
flag=True
while flag:
    if re_com:
        n1=float(input("Enter First Nummber ? :"))
    else:
        n1=result
    op=str(input("Enter the Opreation to do ? Type '+' or '-' or '/' or 'x' : "))
    n2=float(input("Enter Second Nummber ? :"))
    if op=='+':
        result=add(n1,n2)
        print(f"{n1} + {n2} = {result}")
    elif op=='-':
        result=sub(n1,n2)
        print(f"{n1} - {n2} = {result}")
    elif op=='x':
        result=multibly(n1,n2)
        print(f"{n1} x {n2} = {result}")
    elif op == '/':
        result = divide(n1, n2)
        print(f"{n1} / {n2} = {result}")
    else:
        print("invalid Opertion")
        break
    next=input(f"Type 'y' if you want to continue calculating with {result} or Type 'n' to start new calculation or Type 'end' to finish :")
    if next=='y':
        re_com=False
    elif next=='n':
        re_com=True
    else:
        flag=False
