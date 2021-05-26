# py -2 bcbar.py

import requests

# import re
# import time
# import argparse
# from luma.led_matrix.device import max7219
# from luma.core.interface.serial import spi, noop
# from luma.core.render import canvas
# from luma.core.virtual import viewport
# from luma.core.legacy import text, show_message
# from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


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
# print (data)

disp = [0]*38
for x in range(len(data)):
    if x % 2 == 0:
        disp.append(data[x])
        if data[x+1] == None:
            disp.append(data[x+1])
        else:                
            disp.append((data[x+1]).replace(',',''))
# print (disp)

disp = list(filter(lambda a:a != 0, disp))
# print (disp)

#coins_2b_mined = (data[7].replace(',','')) #data[1] is the Coins remaining to be Mined. replace() removes the ',' from the string. int() coverts the string into an into

#coins_2b_mined = data[7]  #Valuw with commas does not look neat on Dot Matrix display.


# serial = spi(port=0, device=0, gpio=noop())
# device = max7219(serial, cascaded=4 , block_orientation=-90, rotate=2)
#
# show_message(device, data[6] + coins_2b_mined, fill="white", font=proportional(LCD_FONT),scroll_delay = 0.04)

##with canvas(device) as draw:
##    text(draw, (0, 0), msg, fill="white", font=proportional(LCD_FONT))
