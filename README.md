# Scraper for allo.ua website


## About
Scraper extracts (name, price, image, description) data for each
product of the website. Data is then serialized into XML format and
saved to a file. Moreover, .xhtml file is formed from newly
created .xml file (data is mapped into a table). 


## Requirements
* Python 3.6 or higher.


## Quickstart
### Linux
1. git clone https://github.com/vsmetansky/allo.git
2. cd allo
3. bash prepare.sh
4. bash start.sh