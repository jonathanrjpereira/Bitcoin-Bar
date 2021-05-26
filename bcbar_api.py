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

from decimal import Decimal, ROUND_HALF_UP

API_URL = 'https://api.coincap.io/v2/assets/'

def round_decimal(x):
  return x.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

def get_price(crypto):
    response = requests.get(API_URL+crypto)
    response_json = response.json()
    return float(response_json['data']['priceUsd'])

def main():
  last_price = -1

  serial = spi(port=0, device=0, gpio=noop())
  device = max7219(serial, cascaded=4 , block_orientation=-90, rotate=2)

  while True:
    crypto = 'bitcoin'
    price = get_price(crypto)
    price_rounded = round_decimal(Decimal(price))

    if price != last_price:
        #might add some msg when price changed? 
        show_message(device, str(price_rounded), fill="white", font=proportional(LCD_FONT),scroll_delay = 0.06)
    else :
        show_message(device, str(price_rounded), fill="white", font=proportional(LCD_FONT),scroll_delay = 0.06)

    last_price = price

main()
