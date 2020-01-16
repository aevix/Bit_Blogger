import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn=None
    try:
        conn = sqlite3.connect(db_file)
        
    except Error as e:
        print(e)
    
    return conn
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, item):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(id, type, size, outgoing) VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, item)
    return cur.lastrowid

def update_item(conn, new_data):

    sql = ''' UPDATE projects
              SET outgoing = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, new_data)
    conn.commit()

def delete_item(conn, id):
    sql = 'DELETE from projects WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def delete_all(conn):
    sql = 'Delete from projects'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def select_all(conn):
    cur = conn.cursor()
    cur.execute('select * from projects')
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_by_id(conn,id):
    sql = 'select * from projects where id =?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = r"C:\Users\April\Documents\GitHub\item_tracker\pythonsqlite.db"
    conn = create_connection(database)

    with conn:
        insert_data(conn, (890809, 'boot', 'large', False))


if __name__ == '__main__':
    main()