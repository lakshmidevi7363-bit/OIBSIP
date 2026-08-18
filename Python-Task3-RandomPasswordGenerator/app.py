import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip


def generate_password():
    try:
        length = int(length_var.get())

        if length < 4:
            messagebox.showwarning(
                "Invalid Length",
                "Password length must be at least 4."
            )
            return

        characters = ""

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning(
                "No Character Type",
                "Please select at least one character type."
            )
            return

        password = "".join(random.choice(characters) for _ in range(length))

        password_var.set(password)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )


def copy_password():
    password = password_var.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    pyperclip.copy(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )



root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x500")
root.resizable(False, False)


title = ttk.Label(
    root,
    text="RANDOM PASSWORD GENERATOR",
    font=("Arial", 20, "bold")
)
title.pack(pady=25)


length_frame = ttk.Frame(root)
length_frame.pack(pady=10)

ttk.Label(
    length_frame,
    text="Password Length:"
).grid(row=0, column=0, padx=10)

length_var = tk.StringVar(value="12")

ttk.Entry(
    length_frame,
    textvariable=length_var,
    width=10
).grid(row=0, column=1)


options_frame = ttk.LabelFrame(
    root,
    text="Character Types",
    padding=15
)
options_frame.pack(pady=20)

lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Checkbutton(
    options_frame,
    text="Lowercase (a-z)",
    variable=lowercase_var
).pack(anchor="w", pady=5)

ttk.Checkbutton(
    options_frame,
    text="Uppercase (A-Z)",
    variable=uppercase_var
).pack(anchor="w", pady=5)

ttk.Checkbutton(
    options_frame,
    text="Numbers (0-9)",
    variable=numbers_var
).pack(anchor="w", pady=5)

ttk.Checkbutton(
    options_frame,
    text="Symbols (!@#$...)",
    variable=symbols_var
).pack(anchor="w", pady=5)

password_var = tk.StringVar()

password_frame = ttk.Frame(root)
password_frame.pack(pady=15)

ttk.Entry(
    password_frame,
    textvariable=password_var,
    width=40,
    justify="center"
).pack()


button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

ttk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password
).grid(row=0, column=0, padx=10)

ttk.Button(
    button_frame,
    text="Copy Password",
    command=copy_password
).grid(row=0, column=1, padx=10)


root.mainloop()