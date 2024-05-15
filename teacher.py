import tkinter as tk
import psycopg2

# MAIN WINDOW
root = tk.Tk()
root.title("School and database")
root.geometry("320x280")
root.resizable(False, False)

# LABELS, ENTRIES
label_general = tk.Label(root, text="Add data")
label_general.grid(row=0, column=1)

label_name = tk.Label(root, text="Name: ")
label_name.grid(row=1, column=0)

entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

root.mainloop()