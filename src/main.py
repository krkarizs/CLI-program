from datetime import datetime, timedelta

class Agent:

    def __init__(self, name_, time_, endtime_, project_):
        
        self.name = name_
        self.starttime = time_
        self.endtime = endtime_
        self.project = project_
        self.metadata = ""
        self.hours = 0
        self.minutes = 0

    def get_metadata(self, string):

        for i in string:
            self.metadata += i

    def get_hours(self, integer):

        self.hours += integer

    def get_minutes(self, integer):

        self.minutes += integer

    def __str__(self):
        return f"Agent {self.name}"


def finish_task():
    while True:
        fullname = input(str("Input your full name: "))

        if len(fullname) < 1:
            print("Error: Must input full name")
            continue

        break
    
    currenttime = datetime.now()
    end_at = tuple(currenttime.timetuple())
    projectname = input(str("Project name: "))

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
    comment = input(str("Comment: "))
    logindata = Agent(fullname, start_at, end_at, projectname)
    logindata.get_metadata(comment)
    logindata.get_hours(workhours)
    logindata.get_minutes(workminutes)

    return logindata

login = finish_task()

print(login.name)
print(login.project)
print(login.metadata)
print(login.starttime)
print(login.endtime)
print(login.hours)
print(login.minutes)