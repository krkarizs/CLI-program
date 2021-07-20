from datetime import datetime, timedelta
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Agent class contains all data from the user when user logs their working hours.
class Agent:

    def __init__(self, name_, time_, endtime_, project_):
        
        self.name = name_
        self.starttime = time_
        self.endtime = endtime_
        self.project = project_
        self.metadata = ""
        self.hours = 0
        self.minutes = 0
        self.totalminutes = 0
        self.totalhours = 0

    def get_metadata(self, string):

        for i in string:
            self.metadata += i

    def get_hours(self, integer):

        self.hours += integer

    def get_minutes(self, integer):

        self.minutes += integer

    def get_totalhours(self, integer1, integer2):
        self.totalhours =  integer1 + (integer2 / 60)

    def get_totalminutes(self, integer1, integer2):
        self.totalminutes = (integer1 * 60) + integer2

    def __str__(self):
        return f"Agent {self.name}"


def finish_task():
    #Get username, handle errors if username is invalid. Username can't be null.
    while True:
        fullname = str(input("Input your full name: "))

        if len(fullname) < 1:
            print("Error: Must input full name")
            continue

        break
    
    #Get current time and format it into a tuple
    currenttime = datetime.now()
    end_at = tuple(currenttime.timetuple())

    #Get project name as a string
    projectname = str(input("Project name: "))

    #Get current time and time worked. Subtract time worked from current time to get start time.
    while True:
        worktime = (input("Time worked (hours and minutes separated by comma): "))
        works = tuple(map(int, worktime.split(',')))

        if len(works) != 2:
            print("Error: Must input hours and minutes as integers")

        if works[0] > 24 or works[0] < 0:
            print("Error: Hours must be within range 0-24")
            continue
        
        if works[1] > 59 or works[1] < 0:
            print("Error: Minutes must be within range 0-59")
            continue

        break
    
    workhours, workminutes = works
    starttime = datetime.now() - timedelta(hours=workhours, minutes=workminutes)
    start_at = tuple(starttime.timetuple())

    #Insert rest of data and return hours and minutes worked.
    comment = str(input("Comment: "))
    logindata = Agent(fullname, start_at, end_at, projectname)
    logindata.get_metadata(comment)
    logindata.get_hours(workhours)
    logindata.get_minutes(workminutes)
    logindata.get_totalhours(logindata.hours, logindata.minutes)
    logindata.get_totalminutes(logindata.hours, logindata.minutes)
    os.system('cls' if os.name == 'nt' else 'clear')

    return logindata

login = finish_task()

""" print(f"Your full name: {login.name}")
print(f"Project worked on: {login.project}")
print(f"Comment: {login.metadata}")
print(f"You started work at {login.starttime[3]}:{login.starttime[4]} {login.starttime[2]}/{login.starttime[1]}/{login.starttime[0]}")
print(f"You finished work at {login.endtime[3]}:{login.endtime[4]} {login.endtime[2]}/{login.endtime[1]}/{login.endtime[0]}")
print(f"You worked for {login.hours}h {login.minutes}m that's {login.totalhours} hours or {login.totalminutes} minutes") """