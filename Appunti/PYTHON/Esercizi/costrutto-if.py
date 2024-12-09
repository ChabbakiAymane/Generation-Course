# Aymmane Chabbaki 09-12-24
print("COSTRUTTO IF 1-2-3")
print("\t[] Scrivi un programma py chiamato costrutto-if.py")
print("\t[] Utilizzando il costrutto if, controlliamo se l'età è minore o uguale a 17 e,\n\t   in tal caso, stampare a video \"Sei minorenne\".")
print("\t[] Utilizzando un altro costrutto if, controllare se l'età è maggiore di 17 e,\n\t   in tal caso, stampare a video \"Sei maggiorenne\".")
print("---------------------------------- START ----------------------------------")
while True:
    # Scelta esercizio 1-2-3 
    scelta = int(input("Scelta es: "))
    match scelta:
        # Se scelta=0, exit dal loop
        case 0:
            break
        # Costrutto if 1
        case 1:
            # Salvo eta utente
            eta = int(input("\tEta': "))
            if(eta <= 17):
                print("\tSei minorenne!")
            if(eta > 17):
                print("\tSei maggiorenne!")
        # Costrutto if 2
        case 2:
            # Salvo eta utente
            eta = int(input("\tEta': "))
            if(eta <= 17):
                print("\tMINORENNE")
            else:
                print("\tMAGGIORENNE")
        # Costrutto if 3
        case 3:
            # Salvo eta utente
            eta = int(input("Eta': "))
            if(eta <= 20):
                print("\tSei giovanissimo!")
            elif(eta >= 21 and eta <= 30):
                print("\tSei giovane!")
            elif(eta >= 31 and eta <= 50):
                print("\tStai diventando vecchio!")
            else:
                print("\tSei... ex giovane!")
print("----------------------------------- END -----------------------------------")