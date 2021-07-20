import psycopg2
from config import config
#import Nikon py

def connect():
    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        #Database opeartions with SQL specified in separate functions


        #Close the connection with the database
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def insert(cursor, arvot):
    cursor.execute(arvot)

if __name__ == '__main__':
    connect()