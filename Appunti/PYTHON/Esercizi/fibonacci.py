# Aymane 09-12-24 pomeriggio
print("FIBONACCI")
print("\t[] la successione di Fibonacci è una successione di numeri interi positivi in cui\n\t   ciascun numero è la somma dei due precedenti e i primi due termini della successione sono\n\tper definizione entrambi di valore 1.")
print("\t[] Progettare e realizzare un programma che stampi la successione di Fibonacci di ordine n,\n\t   con n inserito da tastiera a runtime.")
print("----------------------------------------------- START -----------------------------------------------")
n_fibonacci = 0
genera_fibonacci = True
print("\t[] Inserire [n] per generare la successione oppure [0] per terminare...")
# Ciclo finchè non interrotto con exit
while genera_fibonacci:
    # Converto numero n
    n_fibonacci = int(input("\t[n]: "))
    # Verifico validita' numero
    if(n_fibonacci < 0):
        break
    # Se input 0, stampo ed esco
    elif(n_fibonacci == 0):
        print(f"\t[FIBONACCI]: {n_fibonacci}")
        break
    # Calcolo la sequenza di fibonacci fino ad [num]
    a, b = 0, 1
    print("\tSEQUENZA: [", end=" ")
    for i in range(n_fibonacci-1):
        dump = a + b
        a = b
        b = dump
        print(f"{b}", end=" ")
    print(f"]\n\t[TOTALE]: {b}", end="\n\t-----------------------------------------\n")
print("----------------------------------------------- END -----------------------------------------------")