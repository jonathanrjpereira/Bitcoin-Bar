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
circulation = int(data[1].replace(',','')) #data[1] is the Coins in circulation. replace() removes the ',' from the string. int() coverts the string into an into
#print (circulation)
total_coins = 21000000 #Total Bitcoins ever to be Mined

coins_2b_mined = total_coins - circulation #Number of Bitcoins left to be mined
print (coins_2b_mined)
