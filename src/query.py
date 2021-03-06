import psycopg2
from config import config
import weather
 
def insert(fullname, projectname, logdata):
    #Insert the full name into the agent table (if it is not there yet) - it is possible to add the number of work hours to this table
    add_name = "INSERT INTO agent (name) VALUES (%s) RETURNING id;"
    #Insert the project name into the project table (if it is not there yet) - it is possible to add the total hours spent on this project
    add_project = "INSERT INTO project (name) VALUES (%s) RETURNING id;"
    #Insert the login date/time, the logout date/time and the comment into the third table
    add_time = "INSERT INTO logs (logintime, logouttime, startclock, endclock, worktime, metadata, temperature, agent_id, project_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        #Database opeartions with SQL
        if not check_if_agent_exist(fullname):
            cursor.execute(add_name, (fullname,))
            person_id = cursor.fetchone()[0]
        else:
            cursor.execute("SELECT id FROM agent WHERE name = %s;",(fullname,))
            person_id = cursor.fetchone()
            
        if not check_if_project_exist(projectname):
            cursor.execute(add_project, (projectname,))
            project_id = cursor.fetchone()[0]
        else:
            cursor.execute("SELECT id FROM project WHERE name = %s;", (projectname,))
            project_id = cursor.fetchone()
        
        cursor.execute(add_time, (logdata[0], logdata[1], logdata[2], logdata[3], logdata[4], logdata[5], weather.temp, person_id, project_id))
        #Close the connection with the database
        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        con.rollback()
    finally:
        if con is not None:
            con.close()

def check_if_agent_exist(fullname):
    SQL = "SELECT COUNT(*) FROM agent WHERE agent.name = %s;"
    con = None
    try:
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        cursor.execute(SQL,(fullname,))
        if cursor.fetchone() == (0,):
            cursor.close()
            return False
        else:
            cursor.close()
            return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        con.rollback()
    finally:
        if con is not None:
            con.close()

def check_if_project_exist(projectname):
    SQL = "SELECT COUNT(*) FROM project WHERE project.name = %s;"
    con = None
    try:
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        cursor.execute(SQL, (projectname,))
        if cursor.fetchone() == (0,):
            cursor.close()
            return False
        else:
            cursor.close()
            return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        con.rollback()
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
        SQL = "SELECT logintime AS date, startclock, endclock, worktime, metadata, agent.name AS agent, project.name AS project, temperature FROM logs FULL JOIN agent ON agent_id = agent.id FULL JOIN project ON project_id = project.id WHERE logintime = (SELECT CURRENT_DATE);"
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