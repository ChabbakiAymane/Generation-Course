# Aymane 09-12-24 pomeriggio
print("CONSONANTE O VOCALE")
print("\t[] Creare un programma che prenda in input da tastiera una lettera e\n\t   dica se è una consonante o una vocale a prescindere da maiuscole o\n\t   minuscole.")
print("---------------------------------- START ----------------------------------")
# Prendo in input il carattere in minuscolo
lettera = input("Inserire lettera: ").lower()
# Controllo che sia 1 solo carattere
if(len(lettera) != 1):
    print("\t[ERROR]: Inserire un solo carattere!")
else:
    # Controllo la tipologia di lettera
    if(lettera in "aeiou"):
        print("\t[VOCALE]")
    elif(lettera in "!\\$\"£%&/()=?^-*/+°#@[]\{\}.,:_;§"):
        print("\t[SIMBOLO]")
    elif(lettera in "0123456789"):
        print("\t[NUMERO]")
    else:
        print("\t[CONSONANTE]")
print("----------------------------------- END -----------------------------------")