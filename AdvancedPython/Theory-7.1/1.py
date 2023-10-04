#find all elements byh ID
from bs4 import BeautifulSoup

#sample HTML content
html_content = "<div id = 'content'><p>Hello,World</p><h1> Hi, guys </h1></div>"

#parse HTML
soup = BeautifulSoup(html_content,"html.parser")

#Navigate the HTML tree
d = soup.div
for h1 in d.find_all("h1"):
    print(h1.text)