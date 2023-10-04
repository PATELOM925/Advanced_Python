# find all elements by Class:
# Find the specific elements with the specified class and print its text content

from bs4 import BeautifulSoup

#sample html content
html_content = "<div class='container'><p class = 'text'>Hello, World!</p><p>HI!</p></div>"

#parse the html
soup = BeautifulSoup(html_content, "html.parser")

#Find paragraph with class 'text'
paragraph = soup.find("p", class_= "text")  # find the first <p>element with class "text"
# paragraph = soup.find("div", class_ = "container")

#print the paragraph text
print(paragraph.text)   # OR print(paragraph.p.text)