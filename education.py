from bs4 import BeautifulSoup
import requests

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content)

#life_expectancy = soup('table')[6]

table = soup('table')[6]
 
headers=soup.find("tr", {"class": "lheader"})
print headers

print headers.td.span.contents
print headers.td.div.contents

print soup.tr.contents