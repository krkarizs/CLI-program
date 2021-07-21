import psycopg2
from config import config

def connect():
    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        return (cursor, con)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def close(cursor, con):
    try:
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

#query for all the timelogs, with Join we can also print the names and projekt names
def all_timelogs():
    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        SQL = "SELECT logintime AS date, startclock, endclock, worktime, metadata, agent.name AS agent, project.name AS project FROM logs FULL JOIN agent ON agent_id = agent.id FULL JOIN project ON project_id = project.id WHERE logintime = (SELECT CURRENT_DATE);"
        cursor.execute(SQL)
        row =[]
        row.append(tuple(cursor.fetchone()))
        while row is not None:
            row.append(tuple(cursor.fetchone()))
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
        return row

def total_worktime_agent():
    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        SQL = "SELECT agent.name, SUM(worktime) FROM logs FULL JOIN agent ON agent_id = agent.id GROUP BY agent.name;"
        cursor.execute(SQL)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def total_worktime():
    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        SQL = "SELECT TO_CHAR((SUM(worktime) || ' minute')::interval, 'HH24:MI') AS all_hours FROM logs;"
        cursor.execute(SQL)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()