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

width = disp.width # Creates a variable width that is the entire width of the screen
height = disp.height # Same thing with height
image = Image.new('1', (width, height)) # Defines image
draw = ImageDraw.Draw(image) # Uses image to create the draw variable

while True:
	draw.rectangle((0,0,width,height), outline=0, fill=0) # Fills the screen with a giant black rectangle, essentially resetting it
	accel, mag = lsm303.read() # Defines acceleration
	accel_x, accel_y, accel_z = accel # Splits acceleration into X,Y,Z
	draw.rectangle((0,0,accel_z/8.2,64), outline=1, fill=1) # Draws a rectangle that will change in size based on the Z acceleration
	disp.image(image) # Displays the image
	disp.display() # Puts up the display
