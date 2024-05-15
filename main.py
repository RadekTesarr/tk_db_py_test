import psycopg2

'''CREATE TABLE FUNCTION'''
def create_table():
    conn = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    # CREATE TABLE COMMAND
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS teacher(
                id SERIAL,
                name TEXT,
                age INT,
                address TEXT
    )''')

    conn.commit()
    conn.close()

'''INSERT DATA FUNCTION'''
def insert_data(teacher_name, teacher_age, teacher_address):
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
    cur.execute(query, (teacher_name, teacher_age, teacher_address))

    conn.commit()
    conn.close()

insert_data("Lockhart", 35, "Bradavice")
