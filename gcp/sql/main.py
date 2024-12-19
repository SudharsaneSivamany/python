import os, time, sys
import psycopg2

# Cloud SQL connection details
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")

# Get credentials and create a DB connection

def get_connection():
    return psycopg2.connect(
        host='127.0.0.1',
        port=5432,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

def create_table_if_not_exists(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_table (
                counter INTEGER DEFAULT 0
            )
        """)
        conn.commit()

def insert_or_update_counter(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT counter FROM test_table")
        result = cursor.fetchone()

        if result is None:
            cursor.execute("INSERT INTO test_table (counter) VALUES (1)")
        else:
            cursor.execute("UPDATE test_table SET counter = counter + 1")

        conn.commit()

def get_counter(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT counter FROM test_table")
        result = cursor.fetchone()
        return result[0] if result else None

def main():
    conn = get_connection()
    try:
        create_table_if_not_exists(conn)
        insert_or_update_counter(conn)
        counter = get_counter(conn)
        print(f"Current counter value: {counter}", file=sys.stderr)
    finally:
        conn.close()

if __name__ == '__main__':
    while True:
        time.sleep(30)
        main()