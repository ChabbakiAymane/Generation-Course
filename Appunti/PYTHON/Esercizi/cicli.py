# Aymane 09-12-24 pomeriggio
print("CICLI")
print("\t[] Creare un programma che abbia due variabili (x=o e y=10).")
print("\t[] Il programma deve prima stampare in output x e y, dire se sono\n\t   uguali o diversi, poi incrementare x e decrementare y.")
print("\t[] Quando x e y sono uguali il programma li stampa, dice che sono\n\t   uguali e l'esecuzione termina.")
print("\t[] Utilizzare il ciclo più adatto.")
print("---------------------------------- START ----------------------------------")
x = 0
y = 10
print(f"\t[x:{x} | y:{y}]")
# Controllo se uguali
if(x == y):
    print(f"\t[x:{x} | y:{y}]: sono uguali!")
    exit # forzo uscita programma
elif(x > y):
    print(f"\t{x} > {y}")
else:
    print(f"\t{y} > {x}")
# Aggiorno variabili
x += 1
y -= 1
print("----------------------------------- END -----------------------------------")