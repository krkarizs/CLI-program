import psycopg2
from config import config

def connect():
    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        #Database opeartions with SQL specified in separate functions
        all_timelogs(cursor)
        total_worktime(cursor)
        #Close the connection with the database
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
#query for all the timelogs, with Join we can also print the names and projekt names
def all_timelogs():
    SQL = ""

def total_worktime():
    SQL = "SELECT agent_id, SUM(worktime) FROM Logs GROUP BY agent_id ORDER BY SUM(worktime) DESC;"
    #query for the total working hours
