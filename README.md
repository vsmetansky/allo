# Scraper for allo.ua website


## About
Scraper extracts (name, price, image, description) data for each
product of the website. Data is then serialized into XML format and
saved to a file. Moreover, .xhtml file is formed from newly
created .xml file (data is mapped into a table). 


## Requirements
* Python 3.6 or higher.


## Running scraper
### Linux
1. cd allo
2. bash prepare.sh
3. bash start.sh