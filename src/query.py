import psycopg2
from config import config
#import Nikon py

fullname = "John Doe"
projectname = "Frontend CLI"
logdata = ("2000.12.22", "2000.12.24", 55, "Frontend project")

def insert(fullname, projectname, logdata):
    #Insert the full name into the agent table (if it is not there yet) - it is possible to add the number of work hours to this table
    add_name = "INSERT INTO agent (name) VALUES (%s) RETURNING id;"
    #Insert the project name into the project table (if it is not there yet) - it is possible to add the total hours spent on this project
    add_project = "INSERT INTO project (name) VALUES (%s) RETURNING id;"
    #Insert the login date/time, the logout date/time and the comment into the third table
    add_time = "INSERT INTO logs (logintime, logouttime, worktime, metadata, agent_id, project_id) VALUES (%s, %s, %s, %s, %s, %s)"


    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(**config())
        #Open a cursor to perform database operations
        cursor = con.cursor()
        #Database opeartions with SQL
        cursor.execute(add_name, (fullname, ))
        person_id = cursor.fetchone()[0]

        cursor.execute(add_project, (projectname, ))
        project_id = cursor.fetchone()[0]

        cursor.execute(add_time, (logdata[0], logdata[1], logdata[2], logdata[3], person_id, project_id))
        #Close the connection with the database
        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        con.rollback()
    finally:
        if con is not None:
            con.close()

if __name__ == '__main__':
    insert(fullname, projectname, logdata)