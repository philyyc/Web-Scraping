# Web-Scraping
A repository dedicated for practicing web scraping. The repository is separated into two projects: the weather fetching project using Beautiful Soup HTML parsing package and the stock price fetching project using Scrapy web scraping framework.\
&nbsp;

## Table of contents
1. [Weather project](#weather-project)
2. Stock price project\
&nbsp;

## Weather project

**Specifications and equirements**:
- Programming language: Python
- Python packages required:
    - Beautiful Soup 4
    - Requests
    - Numpy
    - Pandas
- Weather information fetched from: [https://www.weather-forecast.com][reference-1]\
&nbsp;

**Input(s)**:
- The name of a country
    - Can begin with either an uppercase or a lower case letter
    - Can include spaces if a country name contains different parts (ie. United Kingdom)
    - Must be spelled correctly
    - Must not start or end with a space\
&nbsp;

**Output(s)**
- A Pandas DataFrame printed, showing weather information at 100 locations in the input country (actual number of locations depends on the website)
    - Has three columns:
        - City (location)
        - Temperature (temperature in degree Celsius)
        - Weather (ie. clear, cloudy, rain showers)
            - Returns _None_ if the weather is not recognised
    - Includes index
- A CSV file storing the Pandas DataFrame which contains weather information at 100 locations in the input country
    - Must specify file name in weather.py
    - Stores in the same directory as weather.py\
&nbsp;

**Examples**
- Sample 1 (sample_1.csv):
    - Weather information of 100 locations in the United Kingdom
- Sample 2 (sample_2.csv):
    - Weather information of 100 locations in Japan
- Sample 3 (sample_3.csv):
    - Weather information of 100 locations Malaysia
- Sample 4 (sample_4.csv):
    - Weather information of 100 locations in Taiwan\
&nbsp;

**Others**
- Real-time weather information is fetched; however, the fetched data is **NOT** updated automatically

[reference-1]: https://www.weather-forecast.com
