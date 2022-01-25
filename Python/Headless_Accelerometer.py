=======
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSM1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

disp.begin()
disp.clear()
disp.display()
