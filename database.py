import psycopg2

def insert_into_db(data):
    conn = psycopg2.connect(
        dbname="your_db", user="your_user", password="your_password", host="localhost"
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            education TEXT
        )
    """)
    cur.execute("""
        INSERT INTO resumes (name, email, phone, skills, education)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data['name'],
        data['email'],
        data['phone'],
        ', '.join(data['skills']),
        ', '.join(data['education']),
    ))
    conn.commit()
    cur.close()
    conn.close()