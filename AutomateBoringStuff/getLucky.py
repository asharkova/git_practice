#! python3
# lucky.py - Open google search results

import bs4
import requests
import sys
import webbrowser

print('Googling...')    # display text while downloading the Google page
res = requests.get('https://google.com/search?q= ' + ' '.join(sys.argv[1:]))

res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# TODO: Open a browser tab for search results
linkElems = soup.select('.kCrYT a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
