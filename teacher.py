import tkinter as tk
import psycopg2

# MAIN WINDOW
root = tk.Tk()
root.title("School and database")
root.geometry("320x280")
root.resizable(False, False)

# FUNCTIONS
def insert_data(name, age, address):
    conn = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    # INSERT DATA COMMAND
    cur = conn.cursor()    
    query = ('''INSERT INTO teacher(name, age, address)
                VALUES (%s, %s, %s)''')
    cur.execute(query, (name, age, address))

    conn.commit()
    conn.close()

# LABELS, ENTRIES
label_general = tk.Label(root, text="Add data")
label_general.grid(row=0, column=1)

# ADD NAME SECTION
label_name = tk.Label(root, text="Name: ")
label_name.grid(row=1, column=0)

entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

# ADD AGE SECTION
label_age = tk.Label(root, text="Age: ")
label_age.grid(row=2, column=0)

entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

# ADD ADDRESS SECTION
label_address = tk.Label(root, text="Address: ")
label_address.grid(row=3, column=0)

entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1)

# BUTTON
add_button = tk.Button(root, text="Add", command=lambda:insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
add_button.grid(row=4, column=1)


root.mainloop()