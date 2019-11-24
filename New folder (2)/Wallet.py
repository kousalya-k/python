def wallet():
    bal=int(input("Enter the balance"))

    # amt = int(input("Enter the amt to deposit"))
    def deposit(amt):
        nonlocal bal
        bal+=amt
        print("The available balance is ",bal)

    # amt2 = int(input("Enter the amount to spent"))
    def spent(amt2):

        nonlocal bal
        if(bal>amt2):
         bal-=amt2
         print("The available balance after spenting is ",bal)
        else:
            print("Low balance! Please Deposit Money And Spend!!!")

    # amttotrans = int(input("enter amt to transfer"))
    def transfer(wallet,amttotrans):

        nonlocal bal
        if(bal>amttotrans):
            "deposit(amttotrans)"
            bal-=amttotrans
            dic=wallet
            dic["deposit"](amttotrans)
            print("The available balnce is ",bal)

    def available():
        nonlocal bal
        print("The available balance is ",bal)

    dict={"deposit":deposit,"spent":spent,"showbalance":available,"Transfer":transfer}
    return dict


Mywallet=wallet()
"""Mywallet["deposit"]()
Mywallet["spent"]()
Mywallet["showbalance"]()
"""
Mywallet["Transfer"](wallet(40),500)
Wallet2=wallet()
Wallet2["showbalance"]()



