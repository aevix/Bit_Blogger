from flask import Flask, render_template, url_for, request
import item_data_base

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='pythonsqlite.db'


@app.route('/', methods =['POST','GET'])
def index():
    if request.method == 'POST':
        select_id = request.form['barcode']
        new_id = select_by_id(conn, barcode=select_id)
    else:
        pass
    return render_template("item_UI.html")
if __name__=="__main__":
    app.run(debug=True)