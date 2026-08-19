balance = 500000
account = []
def checkbalance(balance):
    print(" Your Current Balance is: ",balance)
def deposit(balance):
    amount = int(input("Enter amount to deposit:"))
    balance = balance + amount
    account.append("Deposited"+str(amount))
    
    return balance,amount
def withdraw(balance):
    amount = int(input("Enter amount: "))
    if amount<=balance:
        balance = balance - amount
        account.append("Withdrawn"+str(amount))
        
    else:
        print("Insufficient Balance")
    return balance,amount
def show_account():
    print(account)
def slip(type, amount, balance):
    print("\n--------------------------")
    print("       ATM RECEIPT")
    print("--------------------------")
    print("Transaction :", type)
    print("Amount      : ₹", amount)
    print("Balance     : ₹", balance)
    print("--------------------------")
    print("   Thank You!")
    print("--------------------------")
last_type = ""
last_amount = 0
while True:
    print("\n1:Check Balance")
    print("2:deposit")
    print("3:withdraw")
    print("4:transcation History")
    print("5:print recepit")
    print("6:Exit")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        checkbalance(balance)
    elif ch == 2:
        balance,last_amount = deposit(balance)
        last_type = "Deposit"
    elif ch == 3:
        balance,last_amount = withdraw(balance)
        last_type = "withdraw"
    elif ch == 4:
        show_account()
    elif ch == 5:
        if last_type !="":
            slip(last_type,last_amount,balance)
        else:
            print("No Transcation yet")
    elif ch == 6:
        print("THANK YOU FOR VISTING US.")
        break
    


