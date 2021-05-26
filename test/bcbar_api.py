
# LED Matrix Prerequisites
import re
import locale
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message, textsize
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

import requests
from decimal import Decimal, ROUND_HALF_UP

# constants
API_URL = 'https://api.coincap.io/v2/assets/'
FONT = proportional(LCD_FONT)
SERIAL = spi(port=0, device=0, gpio=noop())
DEVICE = max7219(SERIAL, cascaded=4 , block_orientation=-90, rotate=2)

def round_decimal(x):
  return x.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

def get_price(crypto):
    response = requests.get(API_URL+crypto)
    response_json = response.json()
    return float(response_json['data']['priceUsd'])

def output_msg(msg):
    w, h = textsize(msg, FONT)
    if w <= DEVICE.width:
        # output fits screen, can show static text.
        x = round((device.width - w) / 2)
        with canvas(device) as draw:
            text(draw, (x, 0), msg, fill="white", font=FONT)
    else:
        # output doesn't fit screen => marquee
        show_message(device, msg, fill="white", font=FONT, scroll_delay=0.06)

def main():
  last_price = -1

  while True:
    crypto = 'bitcoin'
    price = get_price(crypto)
    locale.setlocale(locale.LC_ALL, '')
    price_rounded = "$" + locale.currency(round_decimal(Decimal(price)), grouping=True, symbol=False)

    if price != last_price:
        #might add some msg when price changed?
        output_msg(price_rounded)
    else :
        output_msg(price_rounded)

    last_price = price

main()

