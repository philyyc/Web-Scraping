from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

country = input("Put type in the full name of the country you wish to search: ")
country = country.replace(" ", "-")
# Take country input and replace spaces with hyphens (ie. United Kingdon becomes United-Kingdom)

url = "https://www.weather-forecast.com/countries/{location}".format(location = country)
# Format the URL to include the country input at the end

document = BeautifulSoup(requests.get(url).text, "html.parser")
# Fetch the page's HTML and parse with Beautiful Soup

table = document.find(["ul"], class_="b-list-table top-city-list-per-country")
# Find the table containing weather data

try:
    entries = table.contents
    # Read the children elements of the table
except:
    print("Error, page can not be accessed")
    # Print error message if the URL is invalid

cities = []
temperature = []
weather = []
# Declare lists for storing city names and weather information

"""
for entry in entries:
    sky = entry.find(class_="smallweathercell")["class"][1].replace("smallweathercellday", "")
    weather.append(sky)
    # Identify the number of different weathers (ie. clear, partially cloudy, light rain)

print(np.unique(np.array(weather)))
# Print a list of unique weathers, showing each weather only once
weather = []
# Reset the weather list
"""

for entry in entries:
    sky = entry.find(class_="smallweathercell")["class"][1].replace("smallweathercell", "").replace("day", "").replace("night", "")
    # Find the weather information as a string and extract the weather
    
    if sky == "clear":
        weather.append("Clear")
    elif sky == "cloud":
        weather.append("Cloud")
    elif sky == "lightrain":
        weather.append("Light rain")
    elif sky == "partcloud":
        weather.append("Partially cloudy")
    elif sky == "rainshowers":
        weather.append("Rain showers")
    elif sky == "thunderstorm":
        weather.append("Thunderstorm")
    else:
        weather.append("No data")
    # Compare the weather to weather statuses and append interpretted weathers
    cities.append(entry.find("a").text)
    # Append the city names
    temperature.append(int(entry.find(class_="temp").text))
    # Append the temperatures

data = pd.DataFrame(np.stack((np.array(cities), np.array(temperature), np.array(weather)), axis=1))
# Create a dataframe from the city, temperature and weather data collected
data.to_csv("Weather/sample_3.csv")
# Export the dataframe as a csv file
print(data)