import customtkinter as ctk

root = ctk.CTk()
root.title("Calculator")
root.geometry("500x300")
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

entry1 = ctk.CTkEntry(root, width=100)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = ctk.CTkEntry(root, width=100)
entry2.grid(row=0, column=2, padx=5, pady=5)

operation = None


def set_plus():
    global operation
    operation = "+"


def set_minus():
    global operation
    operation = "-"


def set_multiply():
    global operation
    operation = "*"


def set_division():
    global operation
    operation = "/"


def calculate():
    global operation
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Помилка! Ділення на нуль"
            else:
                result = num1 / num2
        else:
            result = "Оберіть операцію (+, -, *, /)"
    except ValueError:
        result_label.configure(text="Результат: Введіть числа")
        return

    result_label.configure(text=f"Результат: {result}")
    operation = None


equalsbutton = ctk.CTkButton(root, fg_color="blue", text="=", command=calculate, font=("Arial", 16))
equalsbutton.grid(row=2, column=0, columnspan=4, pady=10)

plusbutton = ctk.CTkButton(root, fg_color="green", text="+", command=set_plus, font=("Arial", 16))
plusbutton.grid(row=1, column=0)

minusbutton = ctk.CTkButton(root, fg_color="green", text="-", command=set_minus, font=("Arial", 16))
minusbutton.grid(row=1, column=1)

multiplybutton = ctk.CTkButton(root, fg_color="green", text="*", command=set_multiply, font=("Arial", 16))
multiplybutton.grid(row=1, column=2)

dividebutton = ctk.CTkButton(root, fg_color="green", text="/", command=set_division, font=("Arial", 16))
dividebutton.grid(row=1, column=3)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 24))
result_label.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()