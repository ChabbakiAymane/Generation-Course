# Aymmane Chabbaki 10-12-24
print("TABELLINE")
print("\t[] Stampare tabelline dall'1 al 10.")
print("---------------------------------- START ----------------------------------")
# Creo matrice generale
matrice = []
# Ciclo per riga
for i in range(1, 11):
    # Genero la lista per la riga
    riga = []
    # Calcolo la tabellina
    for j in range(1, 11):
            riga.append(i*j)
    # Aggiungo la lista creata alla matrice principale
    matrice.append(riga)
# Stampo la tabellina
for riga in matrice:
    for num in riga:
        print(f"{num:5}", end="")
    print()
print("----------------------------------- END -----------------------------------")