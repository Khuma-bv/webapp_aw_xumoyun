from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db-xumoyun.clyucs4e44b4.ap-northeast-2.rds.amazonaws.com",
        database="db_xumoyun",
        user="postgres",
        password="Kod990614497"
    )
    return conn

@app.route('/books')
def books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT book, author, sales_millions FROM tbl_xumoyun_books_data ORDER BY sales_millions DESC LIMIT 50;")
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('books.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    book = request.form['book']
    author = request.form['author']
    sales = request.form['sales']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_xumoyun_books_data (book, author, sales_millions) VALUES (%s, %s, %s)",
                (book, author, sales))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/books')

@app.route('/delete', methods=['POST'])
def delete():
    book = request.form['book']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_xumoyun_books_data WHERE book = %s", (book,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/books')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')