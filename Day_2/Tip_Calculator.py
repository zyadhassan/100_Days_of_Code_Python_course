
##Day2: TIP calculator

print('Welcome to the tip calculator.')
bill=float(input("what was the total bill?  $"))
pre=int(input('what precentage tip would you like to give ? 10,12 or 15? '))
bill=bill+(bill*(pre*0.01))
people=int(input('How many people to split the bill?'))
bill_per_p=bill/people
bill_per_p=round(bill_per_p,2)
print(f"Each person should pay: ${bill_per_p}")


