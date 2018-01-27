# py -2 bcbar.py

import requests
page = requests.get("http://www.bitcoinblockhalf.com/")
#print (page.status_code)
#print (page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
#list(soup.children)
#print([type(item) for item in list(soup.children)])

#print(soup.find_all('td'))

#for paragraph in soup.find_all('td'):
#    print (paragraph.string)

data = []
for paragraph in soup.find_all('td'):
    data.append(paragraph.string)
#print data[0]
coins_2b_mined = int(data[7].replace(',','')) #data[1] is the Coins remaining to be Mined. replace() removes the ',' from the string. int() coverts the string into an into
print (coins_2b_mined)
