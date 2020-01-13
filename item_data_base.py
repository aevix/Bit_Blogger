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
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(item_id, type , size, yn)
              VALUES(?,?,?,?) '''
    c = conn.cursor()
    c.execute(sql, statement)
    return c.lastrowid

def main():
    database = r"pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        item = (4548156548, 'suit', 'large', 'y')
        item_id = create_table(conn,item)

if __name__ == '__main__':
    main()