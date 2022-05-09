from requests import get
import folium
import os
import webbrowser
import html


# Defining a colour scale
def colour_grad(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value - minimum) / (maximum - minimum)
    blue_factor = int(max(0, 255 * (1 - ratio)))
    green_factor = int(max(0, 255 * (ratio - 1)))
    red_factor = 255 - blue_factor - green_factor
    hex_color = '#%02x%02x%02x' % (red_factor, green_factor, blue_factor)
    return hex_color


# Defining a better colour scale
def colour_grad_v2(value):
    if value < -50:
        return "#000cff"
    if value < -20:
        return "#0059ff"
    if value < -10:
        return "#00a6ff"
    if value < 0:
        return "#00ffdc"
    if value < 10:
        return "#fff000"
    if value < 20:
        return "#ffc100"
    if value < 50:
        return "#ff7000"
    if value >= 50:
        return "#ff0000"


"""
# Fetching the weather stations
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stationsData = get(url).json()
stations = []

for stationData in stationsData['items']:
    station = {}
    station["name"] = html.escape(stationData['weather_stn_name'])
    station["lat"] = stationData['weather_stn_lat']
    station["lon"] = stationData['weather_stn_long']
    stations.append(station)

# Creating a map
worldMap = folium.Map(location=[0, 0], zoom_start=2)

# Plotting stations
for station in stations:
    folium.Marker([station["lat"], station["lon"]],
                  icon=folium.Icon(icon='cloud', color='blue'),
                  popup=station["name"]).add_to(worldMap)
"""

# Getting station and weather data
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'
stationsData = get(url).json()
stations = []
maxTemperature = -100.0
minTemperature = 100.0

for stationData in stationsData['items']:
    station = {
        "name": html.escape(stationData['weather_stn_name']),
        "lat": stationData['weather_stn_lat'],
        "lon": stationData['weather_stn_long'],
        "temperature": -999
    }
    if 'ambient_temp' in stationData:
        temperature = stationData['ambient_temp']
        if -100 < temperature < 100:
            station["temperature"] = temperature
            if temperature > maxTemperature:
                maxTemperature = temperature
            if temperature < minTemperature:
                minTemperature = temperature
    stations.append(station)
print(minTemperature, maxTemperature)

# Setting up the map
worldMap = folium.Map(location=[0, 0], zoom_start=2)
for station in stations:
    station_color = "#000000"
    if station["temperature"] != -999:
        station_color = colour_grad_v2(station["temperature"])
    folium.CircleMarker((station["lat"], station["lon"]),
                        radius=10,
                        popup=str(station["temperature"]) + "°C at " + station["name"],
                        color=station_color,
                        fill=True,
                        fill_color=station_color).add_to(worldMap)

# Map display
CWD = os.getcwd()
worldMap.save('worldMap.html')
webbrowser.open_new('file://' + CWD + '/' + 'worldMap.html')
