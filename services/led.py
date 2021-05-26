import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message, textsize
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

FONT = proportional(LCD_FONT)
SERIAL = spi(port=0, device=0, gpio=noop())
DEVICE = max7219(SERIAL, cascaded=4 , block_orientation=-90, rotate=2)

def output_msg(msg):
    w, h = textsize(msg, FONT)
    if w <= DEVICE.width:
        # output fits screen, show static text
        x = round((DEVICE.width - w) / 2)
        with canvas(DEVICE) as draw:
            text(draw, (x, 0), msg, fill="white", font=FONT)
    else:
        # output doesn't fit screen => marquee
        show_message(DEVICE, msg, fill="white", font=FONT, scroll_delay=0.06)