from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

'''
print(soup.prettify())
'''
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Website summary: ", item.find("a").parent.parent.find("p").text)  # going to parent element

        '''
        item.children gives the child of item and item.next_sibling
        gives the next sibling. similarly item.previous_sibling gives
        previous sibling
        '''