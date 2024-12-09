# Aymane Chabbaki 05-12-2024
print("VARIABILI, STAMPE, STRINGHE")
print("\t[] Assegna un messaggio a una variabile, poi stampa il messaggio.")
print("\t[] Assegna un messaggio a una variabile, stampa il messaggio, poi cambia\n\t   il messaggio nella variabile e ristampa il messaggio.")
print("\t[] Usa una variabile per rappresentare il nome di una persona e poi stampa un messaggio a quella persona.")
print("\t[] Usa una variabile per rappresentare il nome completo di una persona e poi\n\t   stampa quel nome tutto minuscolo, tutto maiuscolo e title-cased (iniziali maiuscole e resto del nome minuscolo).")
print("---------------------------------- START ----------------------------------")
log_msg = "Questo e' un messaggio log"
print(log_msg)
# Modifico la variabile
log_msg = "Questo e' un messaggio aggiornato"
print(log_msg)
print("---------------------------------------------------------------------------")
# Persona 1
persona1 = "Bruce Wayne"
print("Ciao " + persona1 + ", io so chi sei veramente \"" + persona1.split(" ")[0] + "\"... o dovrei dire BATMAN!")
print("---------------------------------------------------------------------------")
# Persona 2
persona2 = "arthur fleck"
print("minuscolo: " + persona2.lower()) # traformo in minuscolo la stringa
print("MAIUSCOLO: " + persona2.upper()) # traformo in maiuscolo la stringa
print("Title Case: " + persona2.title()) # iniziali in maiuscolo
print("----------------------------------- END -----------------------------------")