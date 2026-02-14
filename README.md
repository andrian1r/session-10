# 🧮 Python Calculator Program

## 📖 Overview

This project is a simple interactive calculator built using Python.

The program allows users to:

- Add numbers
- Subtract numbers
- Multiply numbers
- Divide numbers
- Continue calculations using the previous result

This project demonstrates how to use functions and dictionaries to create a flexible and clean operation system.

---

## 🧠 Concepts Used

- Functions
- Dictionaries
- While loops
- Conditional statements
- User input handling
- Float number operations
- Function references inside dictionaries

---

## ⚙️ How It Works

1. The user enters the first number.
2. The program displays available operation symbols.
3. The user selects an operation.
4. The user enters the second number.
5. The program calculates and displays the result.
6. The user can continue calculating with the previous result or exit.

---

## 💻 Full Code

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    angka_1 = float(input("Masukan angka pertama: "))

    for symbol in operation:
        print(symbol)

    lanjut = True

    while lanjut:
        pilih_operasi = input("Pilih operasi: ")
        angka_2 = float(input("Masukan angka kedua: "))

        calculation_function = operation[pilih_operasi]
        answer = calculation_function(angka_1, angka_2)

        print(f"{angka_1} {pilih_operasi} {angka_2} = {answer}")

        mau_lanjut = input(f"Ketik 'y' untuk lanjut hitung dengan {answer}, atau 'n' untuk selesai: ").lower()

        if mau_lanjut == "y":
            angka_1 = answer
        else:
            lanjut = False
            print("Calculator selesai.")

calculator()
```

---

## 🛠 Requirements

- Python 3.x

---

## 👤 Author

Andrian Wijaya

---

## 📜 License

This project is created for educational purposes.# session-10
A simple Python calculator program using functions and a dictionary-based operation system to perform basic arithmetic calculations interactively.
