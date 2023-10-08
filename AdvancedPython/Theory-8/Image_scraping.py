#scraping images
from bs4 import BeautifulSoup

# Sample HTML content with a table
html_content = "<img src = 'https://example.com/image.jpg' alt='sample image'>"

#parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the image
image = soup.img

#extract and print image source and alt text
src = image["src"]   #source (src)
alt = image["alt"]   #alternative text (alt)
print("Image source:", src)
print("Image Alt Text:", alt)
