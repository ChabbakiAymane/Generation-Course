# Aymane Chabbaki 05-12-2024
print("NUMERIC OPERATIONS: EXERCISE 2")
print("\t[] Write a python program named program.py")
print("\t[] Define a new variable named start_number, with value 30.")
print("\t[] Define 5 new variables (or use 5 times the same), containing the result of 5 different operations involving ‘start_number’\n\t   (one for each variable, or, print and then change the value of the same variable), the result of every operation\n\t   (so the final value in the variable) have to be 5 ( or 5.0) obtained using at least 2 different operators in the operation.")
print("\t[] Print every result.")
print("\t[] Try using some comments in your code to make it clearer.")
print("\t[] Launch your program in console using command python (python3 on unix) and\n\t   be sure it works without errors.")
print("---------------------------------- START ----------------------------------")
# Variabile start_number
start_number = 30
# Operazioni che fanno sempre 5 come risultato partendo da start_number
tmp_var = start_number - 25 # (30-25)=5
print("{} - {} = {}".format(start_number, 25, tmp_var))
tmp_var = start_number / 6 # (30/6)=5.0
print("{} / {} = {}".format(start_number, 6, tmp_var))
tmp_var = start_number % 25 # (30%25)=5
print("{} % {} = {}".format(start_number, 25, tmp_var))
tmp_var = (start_number - 15) / 3 # (15/3)=5
print("({} - {}) / {} = {}".format(start_number, 15, 3, tmp_var))
tmp_var = (start_number + 3) // 6 # (33//6)=5 tronco
print("({} + {}) // {} = {}".format(start_number, 3, 6, tmp_var))
print("----------------------------------- END -----------------------------------")