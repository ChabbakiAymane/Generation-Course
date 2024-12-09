# Aymane 09-12-24 pomeriggio
print("SIMULATE A BANKING SYSTEM")
print("\t[] Simulate a simple banking system where the user can perform the following operations:")
print("\t   • Check balance.")
print("\t   • Deposit money.")
print("\t   • Withdraw money.")
print("\t   • Exit.")
print("\t[] Use a while loop to repeatedly prompt the user for an action until they choose to exit.\n\t   Ensure that the balance cannot go negative.")
print("---------------------------------- START ----------------------------------")
# Saldo prova
balance = 1000
# Continuo while finche utente non EXIT
continue_ops = True
print("MENU OPERAZIONI:\n\t  0. EXIT\n\t  1. CHECK BALANCE\n\t  2. DEPOSIT MONEY\n\t  3. WITHDRAW MONEY")
while continue_ops:
    # Operazione utente
    operazione = int(input("OPERAZIONE: "))
    match operazione:
        # EXIT
        case 0:
            print("\t[EXIT]")
            continue_ops = False
        # SALDO ATTUALE
        case 1:
            print("\t[CHECK BALANCE]")
            print(f"\t[BALANCE] : {balance} $")
        # DEPOSITO SOLDI
        case 2:
            print("\t[DEPOSIT MONEY]")
            money = int(input("\t[DEPOSIT]: "))
            if(money < 0):
                print("\t[INSERT CORRECT AMOUNT OF MONEY]")
            else:
                balance += money
                print(f"\t[DEPOSIT {money} $ DONE]")
        # RITIRO SOLDI
        case 3:
            print("\t[WITHDRAW MONEY]")
            money = int(input("\t[WITHDRAW]: "))
            if(money < 0):
                print("\t[INSERT CORRECT AMOUNT OF MONEY]")
            elif(balance >= money):
                    balance -= money
                    print(f"\t[WITHDRAW {money} $ DONE]")
            else:
                print("\t[BALANCE INSUFFICIENT]")
        # DEFAULT
        case __:
            print("\t[OPERAZIONE SCELTA INESISTENTE]")
print("----------------------------------- END -----------------------------------")