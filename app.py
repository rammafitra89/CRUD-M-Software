from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "90a390c53b6290137696bb99be4f18a3"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'list_of_book'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM KumpulanBuku")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', booklist = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Succesfully")
        Title = request.form['Title']
        Author = request.form['Author']
        Date_Published = request.form['Date_Published']
        Number_of_Pages = request.form['Number_of_Pages']
        Type_of_Book = request.form['Type_of_Book']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO KumpulanBuku (Title, Author, Date_Published, Number_of_Pages, Type_of_Book) VALUES (%s,%s,%s,%s,%s)",(Title,Author, Date_Published,Number_of_Pages, Type_of_Book ))
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method =='POST':
        id_data = request.form['id']
        Title = request.form['Title']
        Author = request.form['Author']
        Date_Published = request.form['Date_Published']
        Number_of_Pages = request.form['Number_of_Pages']
        Type_of_Book = request.form['Type_of_Book']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE KumpulanBuku
            SET Title=%s, Author=%s, Date_Published=%s, Number_of_Pages=%s, Type_of_Book=%s
            WHERE id=%s """,
            (Title, Author, Date_Published, Number_of_Pages, Type_of_Book, id_data))
        flash("Data Update Succesfully")
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['POST','GET'])
def delete(id_data):
    print(id_data, 'test')
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM KumpulanBuku WHERE id = %s", (id_data,))
    flash("Data Deleted Successfully")
    mysql.connection.commit()
    return redirect(url_for('index'))



if __name__ == "__name__":
    app.run(debug=True)