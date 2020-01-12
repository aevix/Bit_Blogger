import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn=None
    try:
        conn = sqlite3.connect(db_file)
        
    except Error as e:
        print(e)
    
    return conn


def create_table(conn, statement):

    sql = ''' INSERT INTO PROJECTS(id, category, size, inorout) VALUES(?,?,?,?) '''
    
    c = conn.cursor()
    c.execute(statement)
    return c.lastrowid

def main():
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        item = ()
    else:
        print("Error! Cannot create the database connection!")

if __name__ == '__main__':
    main()