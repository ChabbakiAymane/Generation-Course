# Aymane Chabbaki 06-12-2024
print("CODE GENERATOR")
print("\t[] Write a python .py program")
print("\t[] Your objective is to create and print a string secret code formatted on this conditions:")
print("\t\t * First and last character of your name.")
print("\t\t * Last two digits of your birth year multiplied by 2.")
print("\t\t * First and third character of a string stored in a variable called secret_word.")
print("\t\t * First 4 characters of your surname.")
print("\t[] Launch your program in console using command python (python3 on unix) and\n\t   be sure it works without errors.")
print("---------------------------------- START ----------------------------------")
# Inserisco i dati che formeranno il secret code generator
name = "Aymane"
surname = "Chabbaki"
year_birth = "1999"
secret_word = "cisco"
formatted_string = name[0].lower() + name[len(name)-1].lower() + "-" + year_birth[2:]*2 + "-" + secret_word[0] + secret_word[2] + "-" + surname[:5].lower()
print("Secret Code:\n\t" + formatted_string)
print("----------------------------------- END -----------------------------------")