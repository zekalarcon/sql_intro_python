import sqlite3
import csv

def create_schema():

    conn = sqlite3.connect('db_libreria.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS libros;")

    cur.execute("""
            CREATE TABLE libros(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [title] TEXT NOT NULL,
                [pags] INTEGER NOT NULL,
                [author] TEXT NOT NULL
            );
            """)

    conn.commit()
    conn.close()

def fill():
    
    with open('libreria.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = list(reader)

        conn = sqlite3.connect('db_libreria.db')
        cur = conn.cursor()

        cur.executemany("INSERT INTO libros (id, title, pags, author) values (NULL, ?, ?, ?)", data)

        conn.commit()
        conn.close()


def fetch(id):
    conn = sqlite3.connect('db_libreria.db')
    cur = conn.cursor()
    try:
        if id == 0:
            for row in cur.execute('SELECT * FROM libros'):
                print(row)
        else:   
            cur.execute("SELECT title, pags, author FROM libros where id=?", str(id))
            row = cur.fetchone()
            print(row) 
    except:
        print('Numero de id no existe')     

    conn.close()      

def search_author(book_title):
    
    conn = sqlite3.connect('db_libreria.db')
    cur = conn.cursor()

    cur.execute("SELECT author FROM libros WHERE title=?", book_title)
    row = cur.fetchone()

    return row


if __name__ == "__main__":
  # Crear DB
    
    create_schema()

  # Completar la DB con el CSV
    
    fill()

  # Leer filas
  # 0 Ver todo el contenido de la DB
  # Cualquier numero para ver fila filtrada por id

    id = 6
    fetch(id)    

  # Buscar autor por book title
    
    book_title = ['El libro de Arena']
    print(search_author(book_title))