# Name: Royce Porogi
# File Name: case_study_if_else_while.py
# Description: This program accepts student names and GPAs and determines
# whether each student qualifies for the Dean's List or Honor Roll.
# Entering ZZZ as the last name will stop the program.
last_name = input("Enter your last name or (ZZZ) to quit: ")
while last_name != "ZZZ":
    first_name = input("Enter your first name: ")
    GPA = float(input("Enter your GPA: "))
    if GPA >= 3.5:
        print(f"{first_name} {last_name} is on the Dean's List.")
    elif GPA >= 3.25:
        print(f"{first_name} {last_name} is on the Honor Roll.")
    else:
        print(f"{first_name} {last_name} is not on the Dean's List or Honor Roll.")
    last_name = input("Enter your last name or (ZZZ) to quit:")    
