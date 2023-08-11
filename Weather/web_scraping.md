## Web Scraping

This is a note summarising how web scraping is done in Python and its key techniques.

Useful references:
- [Tech with Tim's Beautiful SOup tutorial][reference-1]\
&nbsp;

### Set up
To download Beatiful Soup 4
```
pip install beautifulsoup4
```
To import Beatiful Soup 4
```python
from bs4 import BeautifulSoup
```
To download requests
```
pip install requests
```

&nbsp;

## HTML parsing

### Reading HTML files (Beautiful Soup)
To read a HTML file into a Beautiful Soup object
```python
with open("name.html", "r") as f:
    document = BeautifulSoup(f, "html.parser")
```
To display a Beautiful Soup object with indentations in the original HTML file
```python
print(document.prettify())
```
To read the HTML of a website
```python
import requests

# requests.get(url).text is used as an argument
page = BeautifulSoup(requests.get("https://www.fitz.cam.ac.uk/").text, "html.parser")
```
&nbsp;

### Writing to HTML files (Beautiful Soup)
To write to a HTML file
```python
with open("name.html", "w") as f:
    f.write(str(document))
```

### Access HTML elements (Beautiful Soup)
To access the first element with a specific tag name and its inner string
```python
# BeautifulSoupObject.tag
title = document.title

# TagElement.string
text = title.string
```
To access all elements with a specific tag name
```python
containers = document.find_all(["div", "span"])
container = document.find(["div"], text="text")
```
To access the content of a tag element (all tags including non-immediate child tags)
```python
content = container.content
```
To access all elements with a specific class assigned in HTML
```python
buttons = document.find_all(class_="button")
```
To access string(s) matching a specific input string (requires the string to be a perfect match, can not contain other characters)
```python
# use text = string_to_search in find or find_all
text = document.find(text="Instagram")
# Return the match string
text = document.find_all(text="Instagram")
# Return a list of match strings
text = document.find_all(["a"], text="Instagram")
# Return a list of tag element(s)
```
To access string(s) matching a specific regular expression
```python
import re

expression = ducoment.find_all(text=re.compile(regEx))
```
To access the parent element of a matched string or tag element
```python
parent = text.parent
```
To access the child element(s) of a tag element (only the immediate child tags)
```python
child = parent.descendents
children = parent.children
# Return a generator object which can be iterated
```
To access the sibling element(s) of a tag element
```python
next_sib = text.next_sibling
prev_sib = text.previous_sibling
next_obj = text.next_siblings
prev_obj = text.previous_siblings
# Return a generator object which can be iterated
```
To change the inner string of a tag element
```python
# TagElement.string = "New string"
text.string = "Insta"
```
To add or change an attribute of a tag element
```python
text["target"] = "_self"
```
&nbsp;

## Scrapy and spiders

### Scrapy project
To start a scrapy project, proceed to the desired directory and activate the appropriate virtual environment with scrapy installed
```
scrapy startproject project-name
```
To change the shell scrapy uses, download the shell and proceed to settings in scrapy.cfg
```
shell = shell-name
shell = ipython
```
&nbsp;

### Scrapy spider

#### CMD commands
To create a spider, proceed to the spiders folder in the project folder
```
scrapy genspider spider-name url-to-scrape
```
To deploy a spider , proceed to the main project folder
```
scrapy crawl spider-name
```
To deploy a spider and store the yields in a file, proceed to the main project foler
```
scrapy crawl spider-name -0 file-name.csv
scrapy crawl spider-name -0 file-name.json
```
To open the scrapy shell, proceed to the spiders folder
```
scrapy shell
```
&nbsp;

#### Scrapy shell commands

The below scrapy shell commands help to locate the desired information, the spiders can then be customised based on the search and filter results.\
&nbsp;

To fetch and access the reponse from a page
```
fetch("url")
response
```
To access an element on the fetched page using CSS selector
```
response.css("css-selector")
```
To access the HTML of an element
```
response.css("css-selector").get()
```
To access an element using XPath (structure similar to file directory)
```
response.xpath("//tag-name[@css-selector])
```
To access the inner string of an element
```
response.css("css-selector ::text")
```
To access an attribute of an element
```
response.css("css-selector").attrib["attribute-name"]
response.css("css-selecto ::attr(attribute-name)).get()
```
To exit scrapy shell
```
exit
```
&nbsp;

#### Scrapy Python code

Once the desired information is located, the filters can be copied to the parse function under a defined spider in its Python file.\
&nbsp;

To define the parse function which locates and returns the desired information in set formats
```python
def parse(self, response):
    # code to extract information
    yield{
        # yield is used instead of return, to yield a generator object
        # categories of information and their values
    }
```
To define the URL for the next page (for  websites with multiple pages) and the procedures
```python
def parse(self, response):
    # code to extract information
    yield{
        # categories of information and their values
    }

    # check for next page (not shown here)
    next_url = "url"

    yield response.follow(next_url, callback = self.parse)
```
To define the URL for individual pages (for websites with items linked to different pages) and the procedures
```python
def parse(self, response):
    # code to extract information
    for item in items:
        item_url = "url"
        yield response.follow(item_url, callback=self.itemParse)
    
def itemParse(self, response):
    # code to extract information on each page
```





[reference-1]: https://www.youtube.com/watch?v=gRLHr664tXA&list=PLzMcBGfZo4-lSq2IDrA6vpZEV92AmQfJK&pp=iAQB
