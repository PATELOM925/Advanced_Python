import requests
from bs4 import BeautifulSoup

# Define the base URL
BASE_URL = "https://www.indiankanoon.org/"

# Define the search query
SEARCH_QUERY = "THE ADVOCATES ACT, 1961"

# Make a request to the search page
response = requests.get(BASE_URL + "/search/?forminput=" + SEARCH_QUERY)

# Parse the response with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the search results
search_results = soup.find_all("div", class_="search-result")

# Open a .txt file for writing
with open("indiankanoon_documents.txt", "w") as f:
    # Write the header line
    f.write("Title\tURL\n")

    for search_result in search_results:
        title = search_result.find("h3").text
        url = BASE_URL + search_result.find("a")["href"]

        # Write the title and URL to the .txt file
        f.write(title + "\t" + url + "\n")

# Close the .txt file
f.close()
