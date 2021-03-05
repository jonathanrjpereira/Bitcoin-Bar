# py -2 bcbar.py

# Web Scraping Prerequisites
import requests
# LED Matrix Prerequisites
import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


while(1):

    page = requests.get("http://www.bitcoinblockhalf.com/")

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser') #Scrapes entire HTML file


    data = []
    for paragraph in soup.find_all('td'):   #Search for all values of td elements
        data.append(paragraph.string)


    disp = [0]*38   #38 is the length of the list data
    for x in range(len(data)):
        if x % 2 == 0:
            if data[x+1] != None:
                disp.append(data[x])
                disp.append(data[x+1])


    disp = list(filter(lambda a:a != 0, disp)) #For some reason every odd element of the list 'disp' is '0'. This removes all occurences of '0' from the list 'disp'
    disp = list(filter(lambda a:a != None, disp)) #If an element is missing, it shows as 'None' and crashes the script. This removes all occurences of 'None' from the list 'disp'
    #Remove 'list' in Python2.7


    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4 , block_orientation=-90, rotate=2)

    for i in range(len(disp)):
        show_message(device, disp[i], fill="white", font=proportional(LCD_FONT),scroll_delay = 0.02) #Change the value of 'scroll_delay' to change the Scrolling Speed

    #show_message(device, disp[4], fill="white", font=proportional(LCD_FONT),scroll_delay = 0.02) # '4' indicates Displays the number of Bitcoins left to mine.
    #Change this value according to the table to display various data parameters
