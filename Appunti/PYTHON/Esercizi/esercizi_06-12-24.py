# Aymane Chabbaki 06-12-24
print("---------------------------------- START ----------------------------------")
print("Esercizio 1")
print("\tScrivi un programma che chieda all'utente il suo nome usando la funzione\n\tinput e poi stampi un messaggio di saluto del tipo: \"Ciao, [nome]!\".")
# Chiedo e salvo nome
nome = input("\tInserisci nome: ")
print("\tCiao {}, tutto bene?".format(nome))
print("---------------------------------------------------------------------------")
print("Esercizio 2")
print("\tChiedi all'utente di inserire due numeri, somma i due numeri e stampa il risultato.")
num1= int(input("\tInserisci primo addendo: "))
num2= int(input("\tInserisci secondo addendo: "))
print(f"\t{num1} + {num2} = {num1+num2}")
print("---------------------------------------------------------------------------")
print("Esercizio 3")
print("\tChiedi all'utente una parola e poi stampa i primi tre cara<eri della parola.")
parola = input("\tInserisci parola: ")
print(f"\tPrimi 3 caratteri: {parola[:3]}")
print("---------------------------------------------------------------------------")
print("Esercizio 4")
print("\tChiedi all'utente una frase e poi stampa gli ul7mi 5 cara<eri della frase.")
frase = input("\tInserisci frase: ")
print(f"\tUltimi 5 caratteri: {frase[len(frase)-5:]}")
print("---------------------------------------------------------------------------")
print("Esercizio 5")
print("\tChiedi all'utente di inserire un numero, poi stampa il doppio del numero.")
doppio_numero = int(input("\tInserisci numero: "))
print(f"\tIl doppio di {doppio_numero} e' {doppio_numero*2}")
print("---------------------------------------------------------------------------")
print("Esercizio 6")
print("\tChiedi all'utente di inserire una parola e stampa la parola al contrario.")
parola_contrario = input("\tInserisci parola: ")
print("\tReverse: {}".format(parola_contrario[::-1]))
print("---------------------------------------------------------------------------")
print("Esercizio 7")
print("\tChiedi all'utente di inserire due numeri, calcola la loro differenza e stampa il risultato.")
num1= int(input("\tInserisci minuendo: "))
num2= int(input("\tInserisci sottraendo: "))
print(f"\t{num1} - {num2} = {num1-num2}")
print("---------------------------------------------------------------------------")
print("Esercizio 8")
print("\tChiedi all'utente di inserire una frase, poi stampa solo i caratteri con indice pari della frase.")
frase = input("\tInserisci frase: ")
print(f"\tStampa indici pari: {frase[::+2]}")
print("---------------------------------------------------------------------------")
print("Esercizio 9")
print("\tChiedi all'utente due parole e stampa la loro concatenazione.")
parola1= input("\tInserisci parola 1: ")
parola2= input("\tInserisci parola 2: ")
print("\tConcatenazione: {}".format(parola1+parola2))
print("---------------------------------------------------------------------------")
print("Esercizio 10")
print("\tChiedi all'utente di inserire un numero intero e poi calcola il suo quadrato. Stampa il risultato.")
numero= int(input("\tInserisci numero: "))
print(f"\t{numero}^2 = {numero*numero}")
print("---------------------------------------------------------------------------")
print("Esercizio 11")
print("\tChiedi all'utente una frase e stampa la frase senza i primi tre caratteri.")
frase= input("\tInserisci frase: ")
print(f"\tFrase senza primi 3 catteri: {frase[3:]}")
print("---------------------------------------------------------------------------")
print("Esercizio 12")
print("\tChiedi all'utente di inserire una frase e poi stampa solo\n\ti primi 10 caratteri della frase al contrario.")
frase= input("\tInserisci frase: ")
print(f"\tPrimi 10 catteri al contrario: {frase[:10][::-1]}")
print("---------------------------------------------------------------------------")
print("Esercizio 13")
print("\tChiedi all'utente di inserire due numeri, calcola il loro prodoto e stampa il risultato.")
num1= int(input("\tInserisci primo moltiplicando: "))
num2= int(input("\tInserisci secondo moltiplicando: "))
print(f"\t{num1} * {num2} = {num1*num2}")
print("---------------------------------------------------------------------------")
print("Esercizio 14")
print("\tChiedi all'utente di inserire una parola e stampa un messaggio che ripete\n\tla parola 3 volte con un trattino in mezzo.\n\tAd esempio: se la parola è \"ciao\", stampa \"ciao-ciao-ciao\".")
parola= input("\tInserisci parola: ")
print("\tParola da ripetere 3 volte: ", (parola + "-") * 2 + parola)
print("---------------------------------------------------------------------------")
print("Esercizio 15")
print("\tChiedi all'utente di inserire una frase e stampa la frase invertendo\n\tsolo i caratteri con indice dispari.")
frase = input("\tInserisci frase: ")
print(f"\tIndici dispari invertiti:{frase[1::2][::-1]}") 
print("----------------------------------- END -----------------------------------")