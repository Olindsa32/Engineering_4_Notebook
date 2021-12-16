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

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
padding = 2
shape_width = 20
top = padding
bottom = height-padding
x = padding
font = ImageFont.load_default()

while True:
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  draw.text((x, top),    "x: " + str(round(accel_x/107, 3)),  font=font, fill=255)
  draw.text((x, top+20), "y: " + str(round(accel_y/107, 3)), font=font, fill=255)
  draw.text((x, top+40), "z: "  + str(round(accel_z/107, 3)), font=font, fill=255)
  disp.image(image)
  disp.display()
