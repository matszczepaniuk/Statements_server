from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

CREATE_DB = '''CREATE DATABASE messages_library''';

CREATE_USERS_TABLE = '''CREATE TABLE users(
    id serial PRIMARY KEY, 
    username varchar(255) UNIQUE,
    hashed_password varchar(80))''';

CREATE_MESSAGES_TABLE = '''CREATE TABLE messages(
    id SERIAL, 
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
    text varchar(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''';

DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

def create_database():
    try:
        cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        try:
            cursor.execute(CREATE_DB)
            print("Database created")
        except DuplicateDatabase as e:
            print("Database already exists", e)
        cnx.close()
    except OperationalError as e:
        print("Connection Error: ", e)

def create_users_table():
    try:
        cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        try:
            cursor.execute(CREATE_USERS_TABLE)
            print("Table created")
        except DuplicateTable as e:
            print("Such table already exists", e)
        cnx.close()
    except OperationalError as e:
        print("Connection Error: ", e)

def create_messages_table():
    try:
        cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        try:
            cursor.execute(CREATE_MESSAGES_TABLE)
            print("Table created")
        except DuplicateTable as e:
            print("Such table already exists", e)
        cnx.close()
    except OperationalError as e:
        print("Connection Error: ", e)