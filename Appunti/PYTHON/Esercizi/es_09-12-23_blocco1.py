# Aymane 09-12-24
print("ESERCIZIO 1")
print("\t[] Chiedi all'utente di inserire due numeri. Se il primo è maggiore del secondo,\n\t   stampa \"Il primo numero è maggiore\", altrimenti stampa \"Il secondo numero è maggiore o uguale\".")
num1 = int(input("\tInserisci numero 1: "))
num2 = int(input("\tInserisci numero 2: "))
# Trovo maggiore/minore
if(num1 > num2):
    print("\tIl primo numero è maggiore del secondo.")
else:
    print("\tIl secondo numero è maggiore o uguale del primo.")
print("---------------------------------------------------------------------------")
print("ESERCIZIO 2")
print("\t[] Chiedi all'utente un numero intero. Se il numero è divisibile per 3, stampa \"Il numero è divisibile per 3\".\n\t   Altrimenti, se è divisibile per 5, stampa \"Il numero è divisibile per 5\".\n\t   Se non è divisibile né per 3 né per 5, stampa \"Il numero non è divisibile né per 3 né per 5\".")
num_intero = int(input("\tNumero: "))
if(num_intero % 3 == 0):
    print(f"\tIl {num_intero} è divisibile per 3.")
elif(num_intero % 5 == 0):
    print(f"\tIl {num_intero} è divisibile per 5.")
else:
    print(f"\t {num_intero} non è divisibile ne' per 3 ne' per 5.")
print("---------------------------------------------------------------------------")
print("ESERCIZIO 3")
print("\t[] Creare un programma che prenda in input da tastiera tre valori numerici diversi e stampi a video il maggiore e minore.")
num1 = int(input("\tNumero 1: "))
num2 = int(input("\tNumero 2: "))
num3 = int(input("\tNumero 3: "))
if ((num1 != num2) and (num1 != num3) and (num2 != num3)):
    # Trovo MAX e MIN tra i 3 numeri
    maggiore = max(num1, num2, num3)
    minore = min(num1, num2, num3)
    print(f"\tIl numero maggiore è: [{maggiore}]")
    print(f"\tIl numero minore è: [{minore}]")
else:
    print("\tI tre numeri devono essere diversi tra loro.")
print("----------------------------------- END -----------------------------------")

# Operatore ternario if inline
# fai_questo if condizione1 else fai_quest_altro
# messaggio = "Inizia per vocale" if name[0].lower() in "aieou" else "Iniza con consonante"