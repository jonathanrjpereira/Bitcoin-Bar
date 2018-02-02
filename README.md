# *Bitcoin Bar*
Bitcoin Bar is a physical notfication bar which displays real time Bitcoin data.
It can display upto 19 different real time Bitcoin data parameters.

Bitcoin Bar runs on a Raspberry Pi & uses a Dot LED Matrix display.

## Prerequisites
**Hardware:**

 1. Raspberry Pi 3 or Zero W running Python 2.7 or above
 2. Max7219 4in1 Cascaded LED 8x8 Dot Matrix

**Webscraping:**

 1. Requests is an elegant and simple HTTP library for Python.  [Requests Installation & Documentation](http://docs.python-requests.org/en/master/user/install/) 
 2. Beautiful Soup 4 is a Python library for pulling data out of HTML and XML files. [Beautiful Soup Installation & Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

**Python Library for Max7219 LED Matrix:**

Python library interfacing LED matrix displays with the MAX7219 driver (using SPI) on the Raspberry Pi. [Installation](https://luma-led-matrix.readthedocs.io/en/latest/install.html)

## Setup & Configurations
Once all the Prerequisties have been successfully installed, download/clone this GitHub Repository. Connect the Display to the Raspberry Pi as shown in the Schematics. Run the main program `bcbar.py`

Bitcoin Bar can display upto 19 different real time data parameters. These can be configured to be displayed in any order or sequence. 
The main program displays all 19 data parameters sequentially.

Data parameters can be individually displayed & their order can be changed by congifuring the following line in the main program: 

    show_message(device, disp[i], fill="white", font=proportional(LCD_FONT),scroll_delay = 0.02)
The value of  `i` will determine the data parameter being displayed.

Bitcoin Bar can display the following real time data parameters:

|Parameter|Example|i|
|--|--|--|
|Total Bitcoins in circulation|16,840,363|0|
|Total Bitcoins to ever be produced|21,000,000|1|
|Percentage of total Bitcoins mined|80.19%|2|
|Total Bitcoins left to mine|4,159,638|3|
|Total Bitcoins left to mine until next blockhalf|1,534,638|4|
|Bitcoin price (USD)|$8,811.00|5|
|Market capitalization (USD)|$148,380,433,987.50|6|
|Bitcoins generated per day|1,800|7|
|Bitcoin inflation rate per annum|3.98%|8|
|Bitcoin inflation rate per annum at next block halving event|1.80%|9|
|Bitcoin inflation per day (USD)|$15,859,800|10|
|Bitcoin inflation until next blockhalf event based on current price (USD)|$13,521,691,013|11|
|Total blocks|507,229|12|
|Blocks until mining reward is halved|122,771|13|
|Total number of block reward halvings|2|14|
|Approximate block generation time|10.00 minutes|15|
|Approximate blocks generated per day|144|16|
|Difficulty|2,603,077,300,219|17|
|Hash rate|22.00 Exahashes/s|18|
