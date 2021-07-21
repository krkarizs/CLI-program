import psycopg2
from config import config
import main
 
def insert(fullname, projectname, logdata):
    #Insert the full name into the agent table (if it is not there yet) - it is possible to add the number of work hours to this table
    add_name = "INSERT INTO agent (name) VALUES (%s) RETURNING id;"
    #Insert the project name into the project table (if it is not there yet) - it is possible to add the total hours spent on this project
    add_project = "INSERT INTO project (name) VALUES (%s) RETURNING id;"
    #Insert the login date/time, the logout date/time and the comment into the third table
    add_time = "INSERT INTO logs (logintime, logouttime, startclock, endclock, worktime, metadata, agent_id, project_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

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
        
        cursor.execute(add_time, (logdata[0], logdata[1], logdata[2], logdata[3], logdata[4], logdata[5], person_id, project_id))
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
    
if __name__ == '__main__':
    logdata_starttime = f"{main.login.starttime[0]}-{main.login.starttime[1]}-{main.login.starttime[2]}"
    if main.login.starttime[3] < 10:
        alku1 = f"0{main.login.starttime[3]}"
    else:
        alku1 = main.login.starttime[3]
    if main.login.starttime[4] < 10:
        alku2 = f"0{main.login.starttime[4]}"
    else:
        alku2 = main.login.starttime[4]
    logdata_startclock = f"{alku1}:{alku2}"

    logdata_endtime = f"{main.login.endtime[0]}-{main.login.endtime[1]}-{main.login.endtime[2]}"
    if main.login.endtime[3] < 10:
        loppu1 = f"0{main.login.endtime[3]}"
    else:
        loppu1 = main.login.endtime[3]
    if main.login.endtime[4] < 10:
        loppu2 = f"0{main.login.endtime[4]}"
    else:
        loppu2 = main.login.endtime[4]
    logdata_startclock = f"{alku1}:{alku2}"
    logdata_endclock = f"{loppu1}:{loppu2}"
    insert(main.login.name, main.login.project, (logdata_starttime, logdata_endtime, logdata_startclock, logdata_endclock, main.login.totalminutes, main.login.metadata))