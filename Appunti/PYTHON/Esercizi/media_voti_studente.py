# Aymane Chabbaki 10-12-2024 pomeriggio
print("MEDIA VOTI STUDENTE")
print("\t[] Dobbiamo popolare un dizionario in cui le chiavi sono rappresentate dai nomi delli studenti\n\t   e il valore associato è una lista di voti.")
print("\t[] Chiedere in input all'utente di inserire il nome dello studente e successivamente inserire\n\t   i voti fintanto che l'inserimento non è terminato, poi aggiungere chiave (nome) e\n\t   valore (lista dei voti) a un dizionario.")
print("\t[] Una volta terminato l'inserimento, creare un secondo dizionario a partire dal primo che\n\t   contenga soltanto il nome dello studente come chiave e la media dei voti come valore.")
print("\t[] Infine stampare la media totale della classe.")
print("---------------------------------- START ----------------------------------")
# Registro per nome_studente - voti[]
print("\tREGISTRO ELETTRONICO\n\t------------------------------------\n\t  0. EXIT\n\t  1. INSERISCI VOTO STUDENTE\n\t  2. STAMPA MEDIA VOTI STUDENTI\n\t  3. MEDIA TOTALE CLASSE")
print("\t------------------------------------")
# Array che conterrà array (nome_studente - voti[...])
registro_elettronico = {}
while True:
    # Prendo in input la scelta dell'utente
    operazione = input("\tOPERAZIONE: ")
    if not operazione.isdigit(): continue
    match int(operazione):
        # Termina il programma
        case 0:
            print("\t------------------------------------")
            print("\t[EXIT].")
            break
        # Inserimento dati degli studenti
        case 1:
            # Prendo in input nome dello studente
            print("\t------------------------------------")
            nome_studente = input("\tNOME STUDENTE: ").strip().lower()
            # Array associato allo studente
            lista_voti = []
            print("\t------------------------------------")
            print("\t**| exit per uscire |**")
            print("\t------------------------------------")
            while True:
                voto = input(f"\tVoti [{nome_studente.upper()}]: ").strip()
                # Verifico condizione di termine
                if(voto.lower() == "exit"):
                    print("\t------------------------------------")
                    print("\t[EXIT].")
                    print("\t------------------------------------")
                    break
                else:
                    # Verifico se voto valido
                    if(voto.isdigit() and int(voto) < 31 and int(voto) > 17):
                        # Salvo nella lista studente i voti validi
                        lista_voti.append(int(voto))
                    else:
                        print("\t------------------------------------")
                        print("\t[INSERIRE VOTO VALIDO (18-30)].")
                        print("\t------------------------------------")
            # Salvo i tutti i voti dello studente
            registro_elettronico[nome_studente] = lista_voti
        # Stampo studenti e la loro media dei voti
        case 2:
            if(registro_elettronico):
                media_voti_studenti = {studente: sum(voti) / len(voti) if voti else 0 for studente, voti in registro_elettronico.items()}
                print("\t------------------------------------")
                print("\tMEDIA STUDENTI:")
                for nome, media in media_voti_studenti.items():
                    print(f"\t\t{nome.title()}: {media:.2f}")
                print("\t------------------------------------")
            else:
                print("\t------------------------------------")
                print("\t[REGISTRO VUOTO].")
                print("\t------------------------------------")
        # Stampo media totale di tutta la classe
        case 3:
            if(registro_elettronico):
                media_totale_classe = sum(media_voti_studenti.values()) / len(media_voti_studenti)
                print("\t------------------------------------")
                print(f"\t\t[MEDIA CLASSE]: {media_totale_classe:.2f}")
                print("\t------------------------------------")
            else:
                print("\t------------------------------------")
                print("\t[REGISTRO VUOTO].")
                print("\t------------------------------------")
print("----------------------------------- END -----------------------------------")