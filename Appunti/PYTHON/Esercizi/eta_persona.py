# Aymane Chabbaki 06-12-2024
print("ETA' DI UNA PERSONA")
print("\t[] Creare un file .py")
print("\t[] Chiedere all'utente di inserire il proprio nome e età'.")
print("\t[] Il programma deve stampare a video i dati che l'utente ha inserito.")
print("\t[] Successivamente stampare l'età in mesi, poi in giorni, poi in minuti,\n\t   infine in secondi e millisecondi.")
print("\t[] Eseguire lo script dal terminale usando il comando py (python3 su unix) e\n\t   verificare che non ci siano errori nel codice.")
print("---------------------------------- START ----------------------------------")
# Salvo nome
name = input("Inserisci nome: ")
# Ciclo finche' non viene inserita un'età corretta
while True:
    # Salvo età
    age = int(input("Inserisci eta': "))
    # Se eta' valida, esco dal ciclo
    if(age > 10 and age < 120):
        break
    print("Inserire eta' compresa tra [10-120]")
print(f"\t[ NOME: [{name}]\t-\tETA': [{age}] ]")
# Calcolo eta' in vari formati
eta_mesi = age * 12
eta_giorni = eta_mesi * 30
eta_minuti = eta_giorni * 60
eta_secondi = eta_minuti * 60
print(f"\t* Mesi:[{eta_mesi}]\n\t* Giorni:[{eta_giorni}]\n\t* Minuti:[{eta_minuti}]\n\t* Secondi:[{eta_secondi}]")
print("----------------------------------- END -----------------------------------")