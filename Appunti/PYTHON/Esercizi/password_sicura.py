# Aymane 09-12-24 pomeriggio
print("PASSWORD SICURA")
print("\t[] Far inserire la password all'utente finche' non rispetta i seguenti vincoli:")
print("\t   * Lunghezza superiore a 8 caratteri.")
print("\t   * Almeno 2 numeri.")
print("\t   * Almeno un carattere speciale.")
print("\t   * Almeno un carattere maiuscolo.")
print("---------------------------------- START ----------------------------------")
DIM_MIN_PASSWORD = 8
is_PASSWORD_VALIDA = True
while True:
    # Prendo in input la password
    password = input("\tInserire password: ")
    # Controllo lunghezza minima di 8
    if(len(password) < DIM_MIN_PASSWORD): 
        print("\t[ERRORE]: La password deve essere lunga almeno 8 caratteri!")
        is_PASSWORD_VALIDA = False
    # Controllo presenza 2 numeri
    numeri_presenti = sum(carattere.isdigit() for carattere in password)
    if(numeri_presenti < 2): 
        print("\t[ERRORE]: La password deve contenere almeno 2 numeri!")
        is_PASSWORD_VALIDA = False
    # Verifico la presenza di almeno 1 carattere speciale
    caratteri_speciali = "!\"#$%\\&'()*+,-./:;<=>?@[\]^_`{|}~"
    if(not any(carattere in caratteri_speciali for carattere in password)):
        print("\t[ERRORE]: La password deve contenere almeno un carattere speciale!")
        is_PASSWORD_VALIDA = False
    # Verifico la presenza di almeno 1 lettera maiuscola
    if(not any(carattere.isupper() for carattere in password)):
        print("\t[ERRORE]: La password deve contenere almeno un carattere maiuscolo!")
        is_PASSWORD_VALIDA = False
    # Se password ha passato tutti i controlli, stampo e termino
    if(is_PASSWORD_VALIDA):
        # La password ha passato tutti i controlli, e' VALIDA
        print(f"\tPASSWORD: [{password}] e' valida.")
        break
    is_PASSWORD_VALIDA = True
print("----------------------------------- END -----------------------------------")