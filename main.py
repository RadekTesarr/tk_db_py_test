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

create_table