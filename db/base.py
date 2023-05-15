import sqlite3
from pathlib import Path


# СУБД
# sqlite
# MySQL, Postgres, MariaDB

def init_db():
    """Для создания соединения с sqlite БД"""
    # DOCSTRING
    global db, cursor
    DB_NAME = 'db.sqlite'  # .sqlite, .db
    DB_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS survey(
        survey_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        interested TEXT,
        photo TEXT,
        submit TEXT,
        cancel TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        photo TEXT
    )""")
    db.commit()


def delete_products():
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()


# def insert_products():
#     cursor.execute("""INSERT INTO products(name, price, photo)
#         VALUES ('Самый лучший финик', 200, 'images/самый лучший финик.jpeg'),
#         ('Самый дорогой финик', 400, 'images/самый дорогой финик.jpg')
#     """)
#     db.commit()
def insert_product():
    db, cursor = init_db()
    cursor.execute("""
        INSERT INTO products(name, price, image) 
        VALUES ('Самый лучший финик', 200, './images/самый лучший финик.jpg')
    """)
    cursor.execute("""
        INSERT INTO products(name, price, image) 
        VALUES ('Самый дорогой финик', 500, './images/самый дорогой финик.jpg')
    """)
    # cursor.execute("""
    #     INSERT INTO products(name, price, image)
    #     VALUES ('Самый обычный финик', 130, './images/img_1.png')
    # """)
    # cursor.execute("""
    #     INSERT INTO products(name, price, image)
    #     VALUES ('Самый дешевый финик', 20, './images/img_2.png')
    # """)
    db.commit()

def get_products():
    db, cursor = init_db()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()
# def get_products():
#     init_db()
#     cursor.execute("""SELECT * FROM products""")
#     return cursor.fetchall()
'''исправил фсм'''
def insert_survey(data):
    init_db()
    cursor.execute("""
    INSERT INTO survey(name, age, gender, interested, photo, submit, cancel)
        VALUES (:name, :age, :gender, :interested, :photo, :submit, :cancel)

    """, {
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'interested': data['interested'],
        'photo': data['photo'],
        'submit': data['submit'],
        'cancel': data['cancel'],
    })
    db.commit()
def get_data():
    init_db()
    cursor.execute(
        '''
        SELECT * FROM dictionary
        '''
    )
    return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    create_tables()
    insert_product()


