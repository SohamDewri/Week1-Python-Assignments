# ============================================================
#            WEEK 1 PYTHON ASSIGNMENTS & MINI PROJECT
# ============================================================
# Topics:
# 1. Temperature Converter
# 2. Student Grade Calculator
# 3. Even/Odd & Prime Number Checker
# 4. Mini Project - Simple ATM Simulator
# ============================================================


# ============================================================
# ASSIGNMENT 1 : TEMPERATURE CONVERTER
# ============================================================

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def temperature_converter():
    print("\n========== TEMPERATURE CONVERTER ==========")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        c = float(input("Enter Temperature in Celsius: "))
        print("Temperature in Fahrenheit =", round(celsius_to_fahrenheit(c), 2), "°F")

    elif choice == "2":
        f = float(input("Enter Temperature in Fahrenheit: "))
        print("Temperature in Celsius =", round(fahrenheit_to_celsius(f), 2), "°C")

    else:
        print("Invalid Choice")


# ============================================================
# ASSIGNMENT 2 : STUDENT GRADE CALCULATOR
# ============================================================

def student_grade():
    print("\n========== STUDENT GRADE CALCULATOR ==========")

    subjects = int(input("Enter Number of Subjects: "))

    total = 0

    for i in range(1, subjects + 1):
        marks = float(input(f"Enter Marks of Subject {i}: "))
        total += marks

    average = total / subjects

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\nTotal Marks :", total)
    print("Average :", round(average, 2))
    print("Grade :", grade)


# ============================================================
# ASSIGNMENT 3 : EVEN/ODD & PRIME NUMBER CHECKER
# ============================================================

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def even_odd_prime():
    print("\n========== EVEN / ODD & PRIME CHECKER ==========")

    num = int(input("Enter a Number: "))

    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

    if is_prime(num):
        print(num, "is a Prime Number")
    else:
        print(num, "is NOT a Prime Number")


# ============================================================
# MINI PROJECT : SIMPLE ATM SIMULATOR
# ============================================================

balance = 10000
PIN = "1234"


def check_balance():
    global balance
    print("\nCurrent Balance = ₹", balance)


def deposit():
    global balance
    amount = float(input("Enter Deposit Amount: ₹"))
    balance += amount
    print("Deposit Successful.")
    print("Updated Balance = ₹", balance)


def withdraw():
    global balance
    amount = float(input("Enter Withdrawal Amount: ₹"))

    if amount <= balance:
        balance -= amount
        print("Please Collect Your Cash.")
        print("Remaining Balance = ₹", balance)
    else:
        print("Insufficient Balance.")


def atm():
    print("\n========== SIMPLE ATM SIMULATOR ==========")

    pin = input("Enter 4-Digit PIN: ")

    if pin != PIN:
        print("Incorrect PIN.")
        return

    while True:

        print("\n------- ATM MENU -------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank You for Using Our ATM.")
            break

        else:
            print("Invalid Choice")


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n")
    print("==============================================")
    print("      WEEK 1 ASSIGNMENTS & MINI PROJECT")
    print("==============================================")
    print("1. Temperature Converter")
    print("2. Student Grade Calculator")
    print("3. Even/Odd & Prime Number Checker")
    print("4. Simple ATM Simulator")
    print("5. Exit")

    option = input("Enter Your Choice: ")

    if option == "1":
        temperature_converter()

    elif option == "2":
        student_grade()

    elif option == "3":
        even_odd_prime()

    elif option == "4":
        atm()

    elif option == "5":
        print("\nProgram Ended Successfully.")
        break

    else:
        print("Invalid Choice! Try Again.")
