# Aymane 09-12-24 pomeriggio
# Importo libreria 're' per poter lavorare con le REGEX
import re
print("CONTROLLO UTENTE & PASSWORD")
print("\t[] Prendere in input un'email e una passowrd dall'utente.")
print("\t[] Controllare che siano uguali a un'email e una password che salviamo in due variabili")
print("\t   * Consideriamo che l'utente, potrebbe aggiungere degli spazi in più che noi vogliamo ignorare.")
print("\t   * Ignoriamo anche maiuscole e minuscole nell'email.")
print("\t[] Se entrambe sono corrette, stampare «Benvenuto nel programma».")
print("\t[] Altrimenti, stampare un messaggio di errore.")
print("---------------------------------- START ----------------------------------")
# EMAIL e PASSWORD ACCESSO
MAIL_ACCESSO = "administrator@gmail.com"
PASSOWORD_ACCESSO = "password"
# Prendo email e password utente
mail_utente = input("\tE-mail: ")
password_utente = input("\tPassword: ")
print("\t------------------------------------")
# Normalizzo dati
mail_utente = mail_utente.strip().lower()
password_utente = password_utente.strip()
# Verifico validita' email usando REGEX
patternEmail = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
if(not re.match(patternEmail, mail_utente)):
    print("\t[ERRORE]: Inserire e-mail valida!")
else:
    # Verifico credenziali accesso
    if((mail_utente == MAIL_ACCESSO) and (password_utente == PASSOWORD_ACCESSO)):
        print("\tBENVENUTO NEL PROGRAMMA")
    else:
        # Controllo cosa e' sbagliato
        if(mail_utente != MAIL_ACCESSO):
            print(f"\t[ERRORE]: {mail_utente} non riconosciuta!")
        else:
            print("\t[ERRORE]: password errata!")
print("----------------------------------- END -----------------------------------")