#navigate the HTML tree
from bs4 import BeautifulSoup

#sample HTMl content
html_content = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"

#parse the HTMl 
soup = BeautifulSoup(html_content,"html.parser")

#navigate the HTML tree
d = soup.div #selecting div element and assigning to variable d, which allows to nagiagte from div element
for p in d.find_all("p"): #iterating through all <p> elements found within div element
    print(p.text) #printing the text of each <p> element