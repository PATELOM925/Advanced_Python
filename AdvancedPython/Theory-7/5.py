# find all elements by tag:
# parse html content containing an ul list with list items
# find all the list items and print their text contents.

from bs4 import BeautifulSoup

#sample html content
html_content = "<ul><li>Item 1</li><li>Item 2</li></ul>"

#parse the html
soup = BeautifulSoup(html_content, "html.parser")

#Find all the list items in the html content and store 'items'
items = soup.find_all('li')  #return a list of all matching elements
#items = soup.find_all('ul')  #return a list of all matching elements

#print each item
for item in items:
    print(item.text)