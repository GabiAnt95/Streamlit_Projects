import sqlite3
import pandas as pd
import hashlib

def create_connection(db_file):
    
    '''
    Creates a connection to a database
    '''
    conn = None
    conn = sqlite3.connect(db_file)
    conn.commit()

    return conn

def insert_values_to_table(conn, table_name, df):

    cur = conn.cursor()
    fields = ", ".join([e for e in df.columns])
    query = f'Create table if not Exists {table_name} ({fields})'
    cur.execute(query)
    df.to_sql(table_name,conn,if_exists='append',index=False)
    conn.commit()

def delete_table(table_name, conn):
    cur = conn.cursor()
    cur.execute(f"DROP TABLE {table_name}")
    conn.commit()

def create_table_users(conn):
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        password TEXT NOT NULL,
        mail TEXT NOT NULL)
    ''')
    conn.commit()

def add_new_user(user_name, password, mail, conn):
    
    hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users (user_name, password, mail) VALUES ('{user_name}', '{hashed_password}', '{mail}')")
    conn.commit()

conn = create_connection('DataBase/db.sqlite')

create_table_users(conn)
add_new_user('admin', 'Sarandonga!%!")%', 'gabino@jejeje.com', conn)


