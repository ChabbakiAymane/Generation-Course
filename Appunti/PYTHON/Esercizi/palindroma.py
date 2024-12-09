# Aymane 09-12-24 pomeriggio
print("FRASE PALINDROMA")
print("\t[] Una frase palindroma è una frase che sia uguale al suo inverso, ossia se letta da destra sinistra rimanga invariata.")
print("\t[] Scrivere un programma che chieda all'utente di inserire una parola o una frase.")
print("\t[] Verificare che la frase inserita sia palindroma e stampare a video l'esito della verifica.")
print("\t   * Non si può utilizzare la funzione reverse()!.")
print("\t   * Si può utilizzare il metodo delle stringhe replace() per rimuovere gli spazi.")
print("---------------------------------- START ----------------------------------")
frase_palindroma = input("\tInserire [parola | frase]: ")
# Normalizzo i dati (minuscolo, no spazi)
frase_palindroma.strip().lower()
frase_formattata = frase_palindroma.replace(" ", "")
# Inverte la stringa
frase_invertita = ""
for carattere in frase_formattata[::-1]:
    frase_invertita += carattere
# Controllo se palindroma
if(frase_formattata == frase_invertita):
    print("\t[PALINDROMA]")
else:
    print("\t[NON PALINDROMA]")
print("----------------------------------- END -----------------------------------")