import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

while True:
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	draw.rectangle((0,0,accel_z/8.2,64), outline=1, fill=1)
	disp.image(image)
	disp.display()
