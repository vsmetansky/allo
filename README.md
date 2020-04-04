# Scraper for allo.ua website


## About
Scraper extracts (name, price, image, description) data for each
product of the website. Data is then serialized into XML format and
saved to a file. Moreover, .xhtml file is formed from newly
created .xml file (data is mapped into a table). 


## Requirements
* Python 3.6 or higher.


## Install
### Linux
1. git clone https://github.com/vsmetansky/extractor.git
1. cd extractor
2. pip3 install .


## Run
### Linux
1. allo [-h] [-f FILE_NAME] [-n ITEM_NUM] 
