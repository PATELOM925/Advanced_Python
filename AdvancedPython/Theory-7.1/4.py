from bs4 import BeautifulSoup

#scarping a real website
#make http GET request,retrieve HTML content of webpage, adn aprse the html to ectract pape title
import requests #library to make HTTP requests
from bs4 import BeautifulSoup

#make an HTTP GET request
url = "https://dribbble.com/tags/simple%20website"
response = requests.get(url) #HTTP GET request to the url and store response in 'resposne' variable

# print(response.text)

#parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')
#response.text extracts HTML content of the HTTP response

# Extract and print the page title
print("Page Title:", soup.title.text)

# Extract and print attributes of all anchor tags
for link in soup.find_all('a'):
    print("Link Text:", link.text)
    print("Link URL:", link.get('href'))
    print("-------------------------")