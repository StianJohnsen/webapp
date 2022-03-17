from flask import Flask,render_template, url_for
import mysql.connector

list_words = ["Salg", "Kjøp", "Artikkel", "Lekse", "Eksamen", "Vitser"]
list_num = [x for x in range(1, 7)]


mydb = mysql.connector.connect(
    host = 'kark.uit.no',
    user = 'stud_v22_johnsensti',
    password = '8&oe5)W4BPyL8kxYRQfF',
    port = '3306',
    database = 'stud_v22_johnsensti'
)







def return_database(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    users = mycursor.fetchall()
    mycursor.close()
    return users

def add_views(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mycursor.close()









app = Flask(__name__)

@app.route('/')
def start_page():

    return render_template('index.html',num = list_num,words = list_words, zip=zip,users = return_database('select tittel,ingress,dato,id from oppslag'))


@app.route('/kategori/<int:id>')
def test(id):
    return render_template('index.html',num = list_num, words = list_words,zip=zip,kapitell = id, id = id, users = return_database(f'select tittel,ingress,dato,id from oppslag where kategori = {id}'))

@app.route ('/kategori/id/<int:id>')
def heia(id):
    add_views(f'update oppslag set treff = treff +1 where id = {id}')
    return render_template('info_tavle.html', num = list_num, words = list_words,zip=zip,kapitell = id, id = id,users=return_database(f'select oppslagtekst,dato,bruker,treff,id,kategori from oppslag where id = {id}'))




if __name__ == '__main__':
    app.run(debug = True)