import bs4
import requests
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")
print(type(noStarchSoup))