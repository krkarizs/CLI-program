import requests

def readfile(filename, linenum):
    try:
        open_file = open(filename)
    except:
        return "File not found"

    all_lines = open_file.readlines()
    open_file.close()

    import os
    if os.stat(filename).st_size == 0:
        return "Empty file"

    try:
        return all_lines[linenum - 1]
    except:
        return IndexError

api_key = readfile("weatherconfig.ini", 1)
city = "Espoo"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},Finland&appid={api_key}")

dataframe = response.json()

temperature = dataframe["main"]["temp"]
clouds = dataframe["clouds"]["all"]
wind = dataframe["wind"]["speed"]
try:
    rain = dataframe["rain"]["1h"]
except:
    rains = "no rain"

if clouds < 25:
    cloudcover = "clear"
elif clouds < 50:
    cloudcover = "partially cloudy"
elif clouds < 75:
    cloudcover = "mostly cloudy"
else:
    cloudcover = "overcast"

if wind < 4:
    winds = "calm"
elif wind < 6:
    winds = "gentle breeze"
elif wind < 11:
    winds = "moderate breeze"
elif wind < 17:
    winds = "strong winds"
elif wind < 27:
    winds = "gale force winds"
elif wind < 32:
    winds = "storm Winds"
else:
    winds = "Hurricane winds"

if rains != "no rain":
    if rain < 2.6:
        rains = "light rain"
    elif rain < 7.7:
        rains = "moderate rain"
    elif rain < 49:
        rains = "heavy rain"
    else:
        rains = "violent rain"

temp = round(temperature - 273.15, 1)