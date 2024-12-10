# Aymane Chabbaki 10-12-2024 pomeriggio
print("CONTEGGI")
print("\t[] A partire da una stringa, creare un dizionario che ha per chiave le singole\n\t   lettere che compongono la parola (spazi e punteggiatura esclusi) e per valore il\n\t   conteggio delle occorrenze di quella lettera nella parola.")
print("\t[] A partire da una stringa, creare un dizionario che ha per chiave le singole\n\t   parole che compongono la frase (spazi e punteggiatura esclusi) e per valore il\n\t   conteggio delle occorrenze di quella parola nella frase.")
print("---------------------------------- START ----------------------------------")
# Trovo composizione e occorrenze dei caratteri che compongolo la stringa prova
stringa_prova = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum urna et fringilla convallis. Pellentesque habitant morbi tristique."
# Normalizzo stringa
stringa_parsata = stringa_prova.strip().lower().replace(" ", "")
# Dizionario vuoto
dizionario_lettere = {}
for lettera in stringa_parsata:
    # Se gia' presente, incremento contatore, altrimenti 1
    if(lettera in dizionario_lettere):
        dizionario_lettere[lettera] += 1
    else:
        dizionario_lettere[lettera] = 1
print("\tDIZIONARIO LETTERE:")
for lettera, occorrenza in dizionario_lettere.items():
    print(f"\t  {lettera}: {occorrenza}")
# Trovo composizione e occorrenze delle parole che compongolo la stringa prova
frase_prova = "Lorem ipsum dolor sit amet, consectetur consectetur adipiscing elit. Sed vestibulum urna et fringilla convallis. Pellentesque habitant morbi tristique."
# Normalizzo stringa
frase_parsata = frase_prova.lower().replace(".", "").replace(",", "")
# Uso split() per ottenere le parole
parole_frase = frase_parsata.split()
# Dizionario vuoto
dizionario_parole = {}
for parola in parole_frase:
    # Se gia' presente, incremento contatore, altrimenti 1
    if(parola in dizionario_parole):
        dizionario_parole[parola] += 1
    else:
        dizionario_parole[parola] = 1
print("\tDIZIONARIO PAROLE:")
for parola, occorrenza in dizionario_parole.items():
    print(f"\t  {parola}: {occorrenza}")
print("----------------------------------- END -----------------------------------")