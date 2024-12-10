# Aymmane Chabbaki 10-12-24
print("LISTE & INDICI")
print("\t[] Chiedere all'utente di inserire dei valori numerici e salvarli in una lista")
print("\t[] Fare in modo che l'utente possa interrompere l'inserimento quando vuole.")
print("\t[] Stampare soltanto i numeri pari che si trovano in posizione pari e i numeri\n\t   dispari che si trovano in posizione dispari (con posizione si intende in\n\t   relazione all'indice che hanno all'interno della lista).")
print("---------------------------------- START ----------------------------------")
empty = []
print("\t** Per terminare il programma, inserire [-1] **")
while True:
    numero= int(input("\tNumero da inserire: "))
    if(numero == -1): 
        print("\t[END]")
        print("\t---------------------------")
        break
    else:
        empty.append(numero)
# Stampo la lista
print(f"\tLISTA: {empty}".replace(" ", ""))
print("\t---------------------------")
for indice in range(empty):
    if(indice%2 == 0 and empty[indice]%2 == 0):
        print(empty[indice])
    if(indice%2 != 0 and empty[indice]%2 != 0):
        print(empty[indice])
print("----------------------------------- END -----------------------------------")