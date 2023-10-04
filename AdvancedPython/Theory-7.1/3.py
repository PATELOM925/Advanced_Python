#extract attributes : extract 'href' attribute of ananchor tag ('a') element
from bs4 import BeautifulSoup

#sample HTML content
html = "<a href='https://www.google.com/'>Visit Example</a>"

#parse the html
soup = BeautifulSoup(html,"html.parser")

#extract the anchor element
link = soup.a

print("link Text: ",link.text)
print("link URL: ",link['href'])