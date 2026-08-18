import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt


DATABASE = "bmi_records.db"


def create_database():
    """Create the BMI records table if it does not exist."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bmi_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                weight REAL NOT NULL,
                height REAL NOT NULL,
                bmi REAL NOT NULL,
                category TEXT NOT NULL,
                recorded_at TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to create the database.\n\n{error}"
        )


def save_record(name, weight, height, bmi, category):
    """Save a BMI calculation to SQLite."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO bmi_records
            (name, weight, height, bmi, category, recorded_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name,
            weight,
            height,
            bmi,
            category,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        connection.commit()
        connection.close()

        return True

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to save BMI record.\n\n{error}"
        )
        return False



def get_category(bmi):
    """Return the standard BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_bmi():
    """Validate input, calculate BMI and save the result."""

    name = name_entry.get().strip()
    weight_text = weight_entry.get().strip()
    height_text = height_entry.get().strip()

   
    if not name:
        messagebox.showwarning(
            "Input Required",
            "Please enter the user's name."
        )
        return

    
    try:
        weight = float(weight_text)
        height = float(height_text)
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Weight and height must be numeric values."
        )
        return

   
    if weight <= 0:
        messagebox.showerror(
            "Invalid Weight",
            "Weight must be greater than zero."
        )
        return

    if height <= 0:
        messagebox.showerror(
            "Invalid Height",
            "Height must be greater than zero."
        )
        return

   
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    category = get_category(bmi)

   
    result_value.config(text=f"BMI: {bmi}")
    category_value.config(text=category)

   
    category_colors = {
        "Underweight": "#3498db",
        "Normal": "#27ae60",
        "Overweight": "#f39c12",
        "Obese": "#e74c3c"
    }

    category_value.config(
        foreground=category_colors[category]
    )

    # Save record
    save_record(
        name,
        weight,
        height,
        bmi,
        category
    )




def show_history():
    """Display saved BMI records for the selected user."""

    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning(
            "Input Required",
            "Enter a user's name to view their history."
        )
        return

    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT weight, height, bmi, category, recorded_at
            FROM bmi_records
            WHERE LOWER(name) = LOWER(?)
            ORDER BY recorded_at DESC
        """, (name,))

        records = cursor.fetchall()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to read BMI history.\n\n{error}"
        )
        return

    history_window = tk.Toplevel(root)
    history_window.title(f"BMI History - {name}")
    history_window.geometry("750x450")
    history_window.resizable(False, False)

    title = ttk.Label(
        history_window,
        text=f"BMI History for {name}",
        font=("Helvetica", 18, "bold")
    )
    title.pack(pady=15)

    if not records:
        ttk.Label(
            history_window,
            text="No BMI records found for this user.",
            font=("Helvetica", 12)
        ).pack(pady=30)

        return

    columns = (
        "weight",
        "height",
        "bmi",
        "category",
        "date"
    )

    table = ttk.Treeview(
        history_window,
        columns=columns,
        show="headings",
        height=14
    )

    table.heading("weight", text="Weight (kg)")
    table.heading("height", text="Height (m)")
    table.heading("bmi", text="BMI")
    table.heading("category", text="Category")
    table.heading("date", text="Date & Time")

    table.column("weight", width=100, anchor="center")
    table.column("height", width=100, anchor="center")
    table.column("bmi", width=80, anchor="center")
    table.column("category", width=120, anchor="center")
    table.column("date", width=220, anchor="center")

    for record in records:
        table.insert("", tk.END, values=record)

    table.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )




def show_graph():
    """Display the user's BMI trend using Matplotlib."""

    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning(
            "Input Required",
            "Enter a user's name to view the BMI trend."
        )
        return

    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT bmi, recorded_at
            FROM bmi_records
            WHERE LOWER(name) = LOWER(?)
            ORDER BY recorded_at ASC
        """, (name,))

        records = cursor.fetchall()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to load BMI trend.\n\n{error}"
        )
        return

    if not records:
        messagebox.showinfo(
            "No Data",
            "No BMI records found for this user."
        )
        return

    dates = [
        datetime.strptime(
            record[1],
            "%Y-%m-%d %H:%M:%S"
        )
        for record in records
    ]

    bmi_values = [
        record[0]
        for record in records
    ]

    plt.figure(figsize=(9, 5))

    plt.plot(
        dates,
        bmi_values,
        marker="o",
        linewidth=2
    )

    plt.title(f"BMI Trend - {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.show()



def clear_form():
    """Clear all input and result fields."""

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_value.config(text="BMI: --")
    category_value.config(
        text="Category: --",
        foreground="#333333"
    )



root = tk.Tk()

root.title("BMI Calculator")
root.geometry("600x650")
root.resizable(False, False)

create_database()


title_label = ttk.Label(
    root,
    text="BMI CALCULATOR",
    font=("Helvetica", 24, "bold")
)

title_label.pack(pady=(25, 5))

subtitle_label = ttk.Label(
    root,
    text="Track your Body Mass Index",
    font=("Helvetica", 11)
)

subtitle_label.pack(pady=(0, 20))


input_frame = ttk.LabelFrame(
    root,
    text="User Information",
    padding=20
)

input_frame.pack(
    padx=40,
    fill="x"
)


ttk.Label(
    input_frame,
    text="User Name:"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=10
)

name_entry = ttk.Entry(
    input_frame,
    width=35
)

name_entry.grid(
    row=0,
    column=1,
    padx=15,
    pady=10
)


ttk.Label(
    input_frame,
    text="Weight (kg):"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=10
)

weight_entry = ttk.Entry(
    input_frame,
    width=35
)

weight_entry.grid(
    row=1,
    column=1,
    padx=15,
    pady=10
)


ttk.Label(
    input_frame,
    text="Height (m):"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=10
)

height_entry = ttk.Entry(
    input_frame,
    width=35
)

height_entry.grid(
    row=2,
    column=1,
    padx=15,
    pady=10
)


calculate_button = ttk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)

calculate_button.pack(
    pady=25
)


result_frame = ttk.LabelFrame(
    root,
    text="BMI Result",
    padding=20
)

result_frame.pack(
    padx=40,
    fill="x"
)


result_value = ttk.Label(
    result_frame,
    text="BMI: --",
    font=("Helvetica", 20, "bold")
)

result_value.pack(pady=5)


category_value = ttk.Label(
    result_frame,
    text="Category: --",
    font=("Helvetica", 16, "bold")
)

category_value.pack(pady=5)


button_frame = ttk.Frame(root)

button_frame.pack(pady=25)


history_button = ttk.Button(
    button_frame,
    text="View History",
    command=show_history
)

history_button.grid(
    row=0,
    column=0,
    padx=5
)


graph_button = ttk.Button(
    button_frame,
    text="View BMI Trend",
    command=show_graph
)

graph_button.grid(
    row=0,
    column=1,
    padx=5
)


clear_button = ttk.Button(
    button_frame,
    text="Clear",
    command=clear_form
)

clear_button.grid(
    row=0,
    column=2,
    padx=5
)


root.mainloop()