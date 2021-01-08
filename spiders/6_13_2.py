import re
from bs4 import BeautifulSoup
import requests
import csv

response = requests.get("http://blog.itpub.net/26736162/abstract/1/")

# re
# pattern = re.compile('<a target=_blank href="(.*?)" class="w750"><p class="title">(.*?)</p></a>')
# link_list = re.findall(pattern, response.text)

# soup
soup = BeautifulSoup(response.text, features="lxml")
link_list = soup.find_all(name='a', attrs={'class': 'w750'})
links = []
for link in link_list:
    links.append((link.get('href'), link.get_text()))
print(links[0])

# save to csv