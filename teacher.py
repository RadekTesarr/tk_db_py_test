import tkinter as tk
import psycopg2

# main window
root = tk.Tk()
root.title("School and database")
root.geometry("300x280")
root.resizable(False, False)

## FUNCTIONS
# insert data 
def insert_data(name, age, address):
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_address.delete(0, tk.END)

    conn = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    # command 
    cur = conn.cursor()    
    query = ('''INSERT INTO teacher(name, age, address)
                VALUES (%s, %s, %s)''')
    cur.execute(query, (name, age, address))
    conn.commit()
    conn.close()
    display_all()

# search by id 
def search(id):
    conn = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    # command
    cur = conn.cursor()
    query = '''SELECT * FROM teacher WHERE id = %s'''
    cur.execute(query, (id,))
    row = cur.fetchone()
    if row:
        display_search(row)
    else:
        display_search("ID not found")
    conn.commit()
    conn.close()

# listbox search data
def display_search(data):
    listbox = tk.Listbox(root, width=25, height=1)
    listbox.grid(row=8, column=1)
    listbox.insert(0, data)

# display all 
def display_all():
    conn = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    # command
    cur = conn.cursor()
    query = '''SELECT * FROM teacher'''
    cur.execute(query)
    all_data = cur.fetchall()
    listbox = tk.Listbox(root, width=25, height=5)
    listbox.grid(row=9, column=1)

    # scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=9, column=2, sticky="nsw")
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    for one_row in all_data:
        listbox.insert(0, one_row)

display_all()

## ADD DATA SECTION
# general label
label_general = tk.Label(root, text="Add data")
label_general.grid(row=0, column=1)

# add name 
label_name = tk.Label(root, text="Name: ")
label_name.grid(row=1, column=0)

entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

# add age
label_age = tk.Label(root, text="Age: ")
label_age.grid(row=2, column=0)

entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

# add address
label_address = tk.Label(root, text="Address: ")
label_address.grid(row=3, column=0)

entry_address = tk.Entry(root) 
entry_address.grid(row=3, column=1)

# add data button
button_add = tk.Button(root, text="Add", command=lambda:insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
button_add.grid(row=4, column=1)

## SEARCH SECTION
# general label
label_search = tk.Label(root, text="Search data")
label_search.grid(row=5, column=1)

# ID section
label_id = tk.Label(root, text="Search by ID: ")
label_id.grid(row=6, column=0)

entry_id = tk.Entry(root)
entry_id.grid(row=6, column=1)

# search button
button_search = tk.Button(root, text="Search", command=lambda:search(entry_id.get()) if entry_id.get().strip() else None)
button_search.grid(row=6, column=2)

root.mainloop()