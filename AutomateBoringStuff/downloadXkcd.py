# * Loads the XKCD home page
    # - download pages with the requests module
# * Saves the comic image on that page:
    # - find URL of the comic image for a page using BS
    # - download and save the comic image to the hard drive with iter_content()
# * Follows the Previous Comic link:
    # - find URL of the previous Comic link, and repeat
# * Repeats until it reaches the first comic

# downloadXKCD.py - Downloads every single XKCD comic
import requests
import os
import bs4


url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image')
    else:
        comicUrl = "http:{}".format(comicElem[0].get('src'))
        print('Downloading image %s ...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
