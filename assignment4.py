
acc_bal = input("enter your account balance")

if (int(acc_bal)> 1000,000 and int (acc_bal) < 200,000) :
    acc_bal = acc_bal - 25,000
    print("we have deducted ksh 25,000")
elif (int(acc_bal)> 500,000 and int(acc_bal) < 200,000) :
    acc_bal = acc_bal -(0.3*acc_bal)
    print("we have deducted 30 percent from your account")
elif int(acc_bal) > 1000000:
    acc_bal = acc_bal-15,000
    print("we have deducted 15,000 from your account")

