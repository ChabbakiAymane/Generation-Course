# Aymane Chabbaki 06-12-2024
print("DA CELCIUS A FAHRENHEIT")
print("\t[] Creare un file .py")
print("\t[] Chiedere all'utente di inserire la temperatura in gradi Celsius.")
print("\t[] Far stampare la temperatura inserita in gradi Fahrenheit utilizzando la formula di conversione")
print("\t[] Eseguire lo script dal terminale usando il comando py (python3 su unix) e\n\t   verificare che non ci siano errori nel codice.")
print("---------------------------------- START ----------------------------------")
# Salvo nome
print("MENU':\n\t0. EXIT\n\t1. FAHRENHEIT -> CELSIUS\n\t2. CELSIUS -> FAHRENHEIT", end="\n\t--------------------------\n")
# SCELTE 0: exit, 1: F -> C, 2: C -> F
while True:
    scelta = int(input("Scelta: "))
    match scelta:
        case 0:
            print("EXIT")
            break
        # Converto FAHRENHEIT in CELSIUS (°F - 32) × 5/9)
        case 1:
            print("FAHRENHEIT -> CELSIUS")
            gradi_F = float(input("Gradi °F: "))
            print(f"{gradi_F}°F == {(gradi_F - 32) * (5 / 9)}°C");
        # Converto CELSIUS in FAHRENHEIT (°C × 9/5) + 32)
        case 2:
            print("CELSIUS -> FAHRENHEIT")
            gradi_C = float(input("Gradi °C: "))
            print(f"{gradi_C}°C == {(gradi_C * (9 / 5)) + 32}°F");
print("----------------------------------- END -----------------------------------")