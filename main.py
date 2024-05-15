import psycopg2

def create_table():
    conn = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS teacher(
                id SERIAL,
                name TEXT,
                age INT,
                address TEXT
    )''')

    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()    
    cur.execute('''INSERT INTO teacher(name, age, address)
                VALUES ('McGonagallová', 50, 'Bradavice')''')

    conn.commit()
    conn.close()

insert_data()