# db.py model
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn
def get_songs():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM songs")
        songs = cursor.fetchall()
        return songs 
def get_customer_p():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT c.customer_name, c.customer_city FROM customer c, borrower b, loan l WHERE c.customer_name = b.customer_name AND b.loan_number = l.loan_number AND l.branch_name = 'Perryridge';")
        customers = cursor.fetchall()
        return customers   

def get_songs_by_title(title):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM songs WHERE title LIKE %s", ['%' + title + '%'])
        songs = cursor.fetchall()  
        return songs  


def create(songtitle, songartist, songgenre):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO songs (title, artist, genre) VALUES(%s, %s, %s)',
                       (songtitle, songartist, songgenre))
    conn.commit()
    conn.close()