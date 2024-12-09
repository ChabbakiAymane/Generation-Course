# Aymmane Chabbaki 09-12-24
print("PARI & DISPARI")
print("\t[] Scrivi un programma py chiamato pari_dipari.py")
print("\t[] Creare uno script che prenda in input da terminale un numero e stampi a video se è pari o dispari.")
print("---------------------------------- START ----------------------------------")
numero = int(input("Numero: "))
# Controllo resto per vedere se pari o dispari
if((numero % 2) == 0):
    print(f"{numero} e' PARI")
else:
    print(f"{numero} e' DISPARI")
print("----------------------------------- END -----------------------------------")