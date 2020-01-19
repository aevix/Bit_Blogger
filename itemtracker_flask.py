from flask import Flask, render_template, url_for, request
import item_data_base

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='pythonsqlite.db'


def create_connection(db_file):
    conn=None
    try:
        conn = sqlite3.connect(db_file)
        
    except Error as e:
        print(e)

    return conn

@app.route('/', methods =['GET'])
def select_by_id(conn,id):
    database = r"pythonsqlite.db"

    conn = create_connection(database)
    
    sql = 'select * from projects where id =?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__=="__main__":
    app.run(debug=True)