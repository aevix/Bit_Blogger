import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn=None
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)


def create_table(conn, statement):

    try:
        c = conn.cursor()
        c.execute(statement)
    except Error as e:
        print(e)

def main():
    database = r"pythonsqlite.db"

    sql_item_tracker = """CREATE TABLE IF NOT EXISTS item_tracking(
        id integer PRIMARY KEY,
        category text NOT NULL,
        size text,
        inorout text NOT NULL

    ); """
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_item_tracker)
    else:
        print("Error! Cannot create the database connection!")

if __name__ == '__main__':
    main()