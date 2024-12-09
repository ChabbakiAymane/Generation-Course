# Aymane 09-12-24 pomeriggio
print("RETTANGOLO DI ASTERISCHI")
print("\t[] Scrivere un programma che prenda in input due valori b e a.")
print("\t[] Il programma deve stampare un rettangolo di asterischi alto a (altezza) e lungo b (base).")
print("\t[] Stampato il rettangolo pieno, cercare di stampare pure un rettangolo vuoto\n\t   (con asterischi soltanto lungo il perimetro).")
print("---------------------------------- START ----------------------------------")
# Prendo le dimensioni del rettangolo
a = int(input("Valore A (altezza): "))
b = int(input("Valore B (base): "))
print("\tRETTANGOLO PIENO")
# Stampo triangolo pieno
for i in range(a):
    for j in range(b):
        print("* ", end="")
    print()
print("\tRETTANGOLO VUOTO")
# Stampo triangolo vuoto
for i in range(a):
    for j in range(b):
        # Solo perimetro da popolare
        if(i == 0 or i == a-1 or j == 0 or j == b-1):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
print("----------------------------------- END -----------------------------------")