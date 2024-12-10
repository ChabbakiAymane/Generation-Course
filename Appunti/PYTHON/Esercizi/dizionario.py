# Aymane Chabbaki 10-12-2024 pomeriggio
print("DIZIONARIO")
print("\t[] Usa un dizionario per salvare le informazioni su una persona che conosci.\n\t   - Salvane il nome, cognome, eta e la citta in cui vivono.\n\t   - Stampa ogni coppia salavata nel dizionario.")
print("\t[] Usa un dizionario per salvare il numero preferito di varie persone.\n\t   - Pensa a 5 nomi e usali come chiavi nel dizionario.\n\t   - Pensa a un numero preferito per ogni persona e usali come valore.")
print("\t[] Un dizionario python puo' essere usato per modellare un vero e proprio dizionario linguistico (glossario per non confonderci).")
print("\t   - Pensa a cinque parole della programmazione che hai imparato e usale come chiavi nel glossario, salva i loro significati come valori.") 
print("\t   - Stampa ogni parola e il suo significato correttamente formattate.")
print("\t[] Crea un dizionario che contiene i tre fiumi piu' lunghi del mondo associati alla nazione in cui si trovano (es. 'nilo': 'egitto').")
print("\t   - Usa un loop per stamapre una frase riguardo a ogni fiume del tipo \"Il nilo scorre in egitto\".")
print("\t   - Usa un ciclo per stampare ogni fiume nel dizionario.")
print("\t   - Usa un ciclo per stampare il nome di ogni nazione nel dizionario.")
print("---------------------------------- START ----------------------------------")
print("-------------------------------------------------------------------------")
# Dizionario per persona
persona = {
    'nome': 'Aymane',
    'cognome': 'Chabbaki',
    'eta': 25,
    'citta': 'Trento'
}
print("\tNUMERI PREFERITI:")
# print(", ".join(f"{chiave}: {valore}" for chiave, valore in persona.items()))
for chiave, valore in persona.items():
    print(f"\t  {chiave}: {valore}")
print("-------------------------------------------------------------------------")
# Dizionario per numeri preferiti
numeri_preferiti = {
    "Andrea": 7,
    "Davide": 42,
    "Francesco": 3,
    "Gennaro": 15,
    "Alessio": 9
}
print("\tNUMERI PREFERITI:")
for nome in numeri_preferiti:
    print(f"\t  {nome}: {numeri_preferiti.get(nome)}")
print("-------------------------------------------------------------------------")
# Dizionario parole informatica
dizionario_parole = {
    'lista': 'Struttura dati omogenea.',
    'dizionario': 'Struttura dati key-value.',
    'integer': 'Tipo di dato.',
    'variabile': 'Locazione di memoria identificata da un nome.',
    'ciclo': 'Struttura che ripete una serie di istruzioni.'
}
print("\tDIZIONARIO INFORMATICO:")
# Stampa di ogni parola e del suo significato, formattati correttamente
for termine, descrizione in dizionario_parole.items():
    print(f"\t  {termine.upper()}:\n\t    * {descrizione}")
print("-------------------------------------------------------------------------")
# Dizionario fiumi nome-nazione
fiumi = {
    "Adige": "Italia",
    "Amazzoni": "Brasile",
    "Nilo": "Egitto",
    "Lena": "Russia",
    "Senna": "Francia",
    "Mississippi": "Stati Uniti",
    "Indo": "Pakistan, India, Cina",
}
# Stampa key-value del dizionario
print("\tRECAP GEOGRAFIA:")
for fiume, nazione in fiumi.items():
    print(f"\t  * Il fiume principale in [{nazione}] è [{fiume}].")
# Stampo tutti i fiumi nel dizionario
print("\tELENCO FIUMI:")
for fiume in fiumi.keys():
    print(f"\t  * {fiume}")
# Stampo tutte le nazione nel dizionario
print("\tELENCO NAZIONI:")
for nazione in fiumi.values():
    print(f"\t  * {nazione}")
print("----------------------------------- END -----------------------------------")