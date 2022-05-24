


age = input("what is your age?")
gender = input("what gender are you : male/female")

acc_bal = 0
if (int(age) > 25) and (int(age) < 30) :
    acc_bal = acc_bal + 10000 
    print("you have received  ksh 10000")
else:
    print("sorry no money for you")