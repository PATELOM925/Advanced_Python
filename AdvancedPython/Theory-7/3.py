# Beautiful Soup is a python package for parsing html and xml documents.
# it creates a parse tree for parsed pages that can be used to extract data from html

from bs4 import BeautifulSoup

html_content = "<html><head><title>My Web Page</title></head><body><p>Hello,World!</p></body></html>"

soup = BeautifulSoup(html_content, "html.parser")

print("Title: ", soup.title)

print("Paragraph: ", soup.p.text)   #soup.p - return with tag