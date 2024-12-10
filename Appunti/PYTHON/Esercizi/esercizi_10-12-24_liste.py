# Aymmane Chabbaki 10-12-24
print("ESERCIZI LISTE")
print("--------------------------------------------------------------------------- START ---------------------------------------------------------------------------")
print("Esercizio 1: Creazione di una lista.")
print("\t[] Crea una lista chiamata numeri contenente i numeri interi da 1 a 5 e stampa la lista.")
# Creo lista
# lista_numeri = [1,2,3,4,5]
# print(f"\tLISTA: {lista_numeri}")
# Genero lista di 5 elementi
lista_num = list(range(1,6))
print(f"\tLISTA: {lista_num}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 2: Accesso agli elementi della lista.")
print("\t[] Data una lista animali = [\"gatto\", \"cane\", \"pesce\", \"uccello\"].\n\t[] Stampa il primo e l'ultimo elemento della lista.")
lista_animali = ["gatto", "cane", "pesce", "uccello", "tigre"]
# Trovo primo e ultimo elemento
primo = lista_animali[0]
ultimo = lista_animali.pop()
print(f"\tPRIMO:[{primo}]\n\tULTIMO:[{ultimo}]")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 3: Modifica della lista.")
print("\t[] Usa la lista colori = [\"rosso\", \"blu\", \"verde\"].\n\t[] Cambia il valore del secondo elemento in \"giallo\" e stampa la lista aggiornata.")
lista_colori = ["rosso", "blu", "verde"]
print(f"\tPRIMA: {lista_colori}")
# Modifico posizione 1 = "giallo"
lista_colori[1] = "giallo"
print(f"\tDOPO : {lista_colori}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 4: Aggiungere e rimuovere elementi")
print("\t[] Crea una lista vuota chiamata frutta.\n\t[] Aggiungi i frutti \"mela\", \"banana\" e \"arancia\".\n\t[] Rimuovi \"banana\" e stampa la lista finale.")
lista_frutta2 = ["mela", "banana", "arancia"]
print(f"\tPRIMA: {lista_frutta2}")
# Elimino posizione 2 = "banana"
del lista_frutta2[1]
print(f"\tDOPO : {lista_frutta2}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 5: Iterazione con le liste")
print("\t[] Dato una lista numeri = [1, 2, 3, 4, 5].\n\t[] Scrivi un ciclo che calcola e stampa il quadrato di ogni numero nella lista.")
lista_numeri = [1, 2, 3, 4, 5]
for elem in lista_numeri:
    print(f'\t    {elem}^2 = {elem * elem}')
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 6: Ordinamento di una lista")
print("\t[] Dato una lista di numeri numeri = [4, 1, 3, 5, 2].\n\t[] Ordina la lista in ordine crescente e decrescente, e stampa entrambi i risultati.")
lista_numeri2 = [4, 1, 3, 5, 2]
# Uso sorted() per non dover dichiare una nuova variabile
print(f"\tSORTED: {sorted(lista_numeri2)}\n\tUNSORTED: {sorted(lista_numeri2, reverse=True)}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 7: Filtraggio di una lista")
print("\t[] Dato una lista di numeri numeri = [10, 15, 20, 25, 30, 35].\n\t[] Crea una nuova lista contenente solo i numeri pari e stampala.")
lista_numeri3 = [10, 15, 20, 25, 30, 35]
nuova_lista = []
for elem in lista_numeri3:
    if(elem % 2 == 0):
        nuova_lista.append(elem)
# Stampo le liste
print(f"\tLISTA: {lista_numeri3}\n\tLISTA PARI: {nuova_lista}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 8: Operazioni con sottoliste")
print("\t[] Dato una lista di nomi nomi = [\"Anna\", \"Luca\", \"Paolo\", \"Elena\", \"Marco\"].\n\t[] Estrai i primi tre nomi in una nuova lista e stampa entrambi gli elenchi.")
lista_nomi = ["Anna", "Luca", "Paolo", "Elena", "Marco"]
# Slicing per ottenere i primi 3
print(f"\tLISTA: {lista_nomi}\n\tPRIMI 3 ELEMENTI: {lista_nomi[:3]}\nULTIMI 2 ELEMENTI: {lista_nomi[3:]}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 9: Liste nidificate")
print("\t[] Crea una lista chiamata matrice che rappresenta la seguente matrice:\n\t    1 2 3\n\t    4 5 6\n\t    7 8 9\n\t[] Stampa il numero nella seconda riga e terza colonna.")
lista_matrice = [[1,2,3],[4,5,6],[7,8,9]]
print(f"\tM[2][3] : {lista_matrice[1][2]}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Esercizio 10: Generazione e analisi")
print("\t[] Usa una comprensione di lista per creare una lista contenente i quadrati dei numeri da 1 a 20.\n\t[] Trova e stampa:\n\t     • Il numero massimo\n\t     • Il numero minimo\n\t     • La somma di tutti i numeri nella lista.")
base = [x for x in range(1, 21)]
quadrati = [x**2 for x in range(1, 21)]
massimo = max(quadrati)
minimo = min(quadrati)
# Uso sum() al posto di for(...)
somma = sum(quadrati)
print(f"\tLISTA\t\t: {base}\n\tLISTA QUADRATI\t: {quadrati}\n\tMAX\t\t: {massimo}\n\tMIN\t\t: {minimo}\n\tSOMMA\t\t: {somma}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")