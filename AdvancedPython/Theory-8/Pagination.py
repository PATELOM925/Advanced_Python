import requests
from bs4 import BeautifulSoup

#Web scraping multiple pages with pagination
for page in range(1,4):  #assuming there r 3 pages
    #contruct url for each page
    url = f"https://example.com/page/{page}"  # "https://example.com/page/1,"  "https://example.com/page/2," and "https://example.com/page/3"
    response = requests.get(url)
    #check if request was successful
    soup = BeautifulSoup(response.text, "html.parser")
    # now extract and process data from each page
    # (e.g., extract items, navigate to the next page)

    #e.g. extract and print text from <p> elements
    print("_______________________")
    print(f"Paragraphs in URL{page}>>>")
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        print(paragraph.text)

    #Extract  and print text from headings <h1> and <h2>
    print(f"Headings in URL{page}>>>")
    headings = soup.find_all(["h1", 'h2'])
    for heading in headings:
        print(heading.text)
    print(f"Scraping done for url{page}")