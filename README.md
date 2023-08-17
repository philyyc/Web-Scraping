# Web-Scraping
A repository dedicated for practicing web scraping. The repository is separated into two projects: the weather fetching project using Beautiful Soup HTML parsing package and the stock price fetching project using Scrapy web scraping framework.\
&nbsp;

## Table of contents
1. [Weather project](#weather-project)
2. [Stock price project](#stock-price-project)\
&nbsp;

## Weather project

**Specifications and requirements**:
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

## Stock price project

**Specifications and requirements**:
- Programming language: Python
- Python packages required:
    - Scrapy
    - iPython (Scrapy shell)
- Stock price information fetched from: [https://site.financialmodelingprep.com/][reference-2]\
&nbsp;

**Input(s)**:
- Company name (required), to fetch stock information for
    - Company name is given by the user when calling the Scrapy spider in the terminal
```
scrapy crawl FinanceModeling -a company="name"
```
- File type (optional), to save the fetched data as
    - File type is given by the user when calling the Scrapy spider in the terminal
```
scrapy crawl FinanceModeling -a company="name" -O file_name.file_type
```
&nbsp;

**Output(s)**
- Various statistics and information on the scrape, printed in the terminal
- Dictionaries containing the following information for each search result found using the company name input:
    - Type (ie. stock, fund, cryptocurrency)
    - Abbreviation
    - Name
    - Price (in USD)
    - Change in value (in USD)
    - Percentage change in value
    - Average volume
    - Market cap
    - Return on equity
    - Return on assets
    - Price-to-earnings ratio
    - Price-to-book ratio\
- A file storing the dictionaries containing individual stock information
    - File type and name specified by the user when calling the Scrapy spider
&nbsp;

**Examples**
- Currently no examples available\
&nbsp;

**Others**
- Real-time stock information is fetched; however, the fetched data is **NOT** updated automatically
- Fields in the return dictionary **MAY BE EMPTY** if relevant information can not be fetched\
&nbsp;

&nbsp;

---
Project created by Yao-Chung (Phil) Yeh

[reference-1]: https://www.weather-forecast.com
[reference-2]: https://site.financialmodelingprep.com/
