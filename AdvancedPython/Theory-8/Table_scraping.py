#Scraping Tables

from bs4 import BeautifulSoup

# Sample HTML content with a table
html_content = "<table><tr><th>Name</th><th>Age</th></tr><tr><td>Alice</td><td>25</td></tr><tr><td>Bob</td><td>30</td></tr></table>"

#parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find first table element in parsed html
table = soup.find("table")

#extract and print table data
for row in table.find_all("tr")[1:]:  #Iterates over the rows, starting from second row (index 1) as first row typically contains header info.
    columns = row.find_all("td")
    name = columns[0].text
    age = columns[1].text
    print(f"Name : {name}, Age: {age}")
