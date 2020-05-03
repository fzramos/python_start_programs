"""
    Goal: Print out the headlines from the current NY Times website to the user
    Utilizing non-standard libraries
    bs4 = Beautiful Soup which is a library for reading(ie parsing) the HTML text
    requests = Library for reading HTML for humans, will get HTML from website and allow us to use it in python
"""
# use this syntax as described on the documentation page: 
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
from bs4 import BeautifulSoup

import requests

#base url to be analyzed
url = "https://www.nytimes.com/"

#Asking website for HTML and saves it as a string
r = requests.get(url)
r_html = r.text

#Parsing the HTML text 
#Note: don't need html.parser arg but adding it gets rid of annoying warning
soup = BeautifulSoup(r_html, "html.parser")

#find and loop through all elements on the page with the
#class name "css-1cmu9py esl82me0" found by inspecting the HTML of the website
for story_heading in soup.find_all(class_ ="css-1cmu9py esl82me0"):
    print(story_heading.contents[0])

#Headlines of NYTIMES except formatted differently and under different class on website for some reason
for story_heading2 in soup.find_all(class_ ="css-1vvhd4r esl82me0"):
    print(story_heading2.get_text(strip = True))
