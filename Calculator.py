import customtkinter as ctk

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Calculator")
root.geometry("350x350")
root.resizable(False, False)
entry1 = ctk.CTkEntry(root, width=125,height=45,font=("Arial",24))
entry1.place(x = 40, y = 20)

entry2 = ctk.CTkEntry(root, width=125,height=45,font=("Arial",24))
entry2.place(x = 185, y = 20)

operation = None


def set_plus():
    global operation
    operation = "+"
    operation_label.configure(text="+")


def set_minus():
    global operation
    operation = "-"
    operation_label.configure(text="-")


def set_multiply():
    global operation
    operation = "*"
    operation_label.configure(text="*")


def set_division():
    global operation
    operation = "/"
    operation_label.configure(text="/")

def clear():
    entry1.delete(0, "end")
    entry2.delete(0,"end")
    result_label.configure(text="")

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
                result = round(result, 5)
        else:
            result = "Оберіть операцію (+, -, *, /)"
    except ValueError:
        result_label.configure(text="Введіть числа")
        return

    result_label.configure(text=f"Результат: {result}")
    operation_label.configure(text="")
    operation = None


equalsbutton = ctk.CTkButton(root, fg_color="blue", text="=",height = 130,width=45, command=calculate, font=("Arial", 16))
equalsbutton.place(x= 265, y = 150)

plusbutton = ctk.CTkButton(root, fg_color="green", text="+", command=set_plus, font=("Arial", 20),width=75, height=65,)
plusbutton.place(x=40,y = 150)

minusbutton = ctk.CTkButton(root, fg_color="green", text="-", command=set_minus, font=("Arial", 20),width=75, height=65,)
minusbutton.place(x=125,y = 150)

multiplybutton = ctk.CTkButton(root, fg_color="green", text="*", command=set_multiply, font=("Arial", 20),width=75, height=65,)
multiplybutton.place(x=40,y = 220)

dividebutton = ctk.CTkButton(root, fg_color="green", text="/", command=set_division, font=("Arial", 20),width=75, height=65,)
dividebutton.place(x=125,y = 220)

clearbutton = ctk.CTkButton(root,fg_color="grey",text = "C", command=clear,height=130,width=45)
clearbutton.place(x=210,y = 150)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 24))
result_label.place(x = 90, y = 80)

operation_label = ctk.CTkLabel(root, text="", font=("Arial", 20))
operation_label.place(x=165, y=100)

root.mainloop()