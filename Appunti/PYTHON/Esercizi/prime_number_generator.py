# Aymane 09-12-24 pomeriggio
# Import della libreria MATH per la funzione sqrt()
import math
print("PRIME NUMBER GENERATOR")
print("\t[] Write a program that generates prime numbers up to a specified number n.")
print("\t[] Use a for loop to iterate through numbers from 2 to n and a while loop to check for prime numbers.")
print("\t[] Print each prime number.")
print("---------------------------------- START ----------------------------------")
# N da generare
n = int(input("\tInserisci n: "))
# Stampa i numeri primi fino a n
print(f"\tNumeri primi fino a {n}:")
for numero in range(2, n + 1):
    i=2
    is_primo = True
    # Verifico divisibilità fino del numero
    while(i <= math.sqrt(numero)):
        if(numero % i == 0):
            is_primo = False
            break
        i+=1
    if(is_primo):
        print(f"\t  [] {numero} e' primo.")
print("----------------------------------- END -----------------------------------")