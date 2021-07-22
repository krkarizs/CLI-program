import psycopg2

def create_tables():
    con = None
    try:
        #Connect to an existing databese
        con = psycopg2.connect(user="postgres",database="workplace")
        #Open a cursor to perform database operations
        cursor = con.cursor()
        SQL = "CREATE TABLE agent (id SERIAL PRIMARY KEY, name varchar(255) NOT NULL);"
        cursor.execute(SQL)
        SQL2 = "CREATE TABLE project (id SERIAL PRIMARY KEY, name varchar(255) NOT NULL);"
        cursor.execute(SQL2)
        SQL3 = "CREATE TABLE Logs (id SERIAL PRIMARY KEY, logintime DATE, logouttime DATE NOT NULL, startclock TEXT NOT NULL, endclock TEXT NOT NULL, worktime INT NOT NULL, metadata varchar(255) NOT NULL);"
        cursor.execute(SQL3)
        SQL4 = "ALTER TABLE Logs ADD agent_id int;"
        cursor.execute(SQL4)
        SQL5 = "ALTER TABLE Logs ADD project_id int;"
        cursor.execute(SQL5)
        SQL6 = "ALTER TABLE Logs ADD CONSTRAINT fk_agent_id FOREIGN KEY (agent_id) REFERENCES agent(id);"
        cursor.execute(SQL6)
        SQL7 = "ALTER TABLE Logs ADD CONSTRAINT fk_project_id FOREIGN KEY (project_id) REFERENCES project(id);"
        cursor.execute(SQL7)

        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        con.rollback()
    finally:
        if con is not None:
            con.close()

create_tables()

