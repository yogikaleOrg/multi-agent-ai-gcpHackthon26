import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )


def save_task(title, priority):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks (title, priority) VALUES (%s, %s)",
        (title, priority)
    )

    conn.commit()
    cur.close()
    conn.close()


def save_note(content):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO notes (content) VALUES (%s)",
        (content,)
    )

    conn.commit()
    cur.close()
    conn.close()