#!/usr/bin/python3

import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306

#def animate()
    
i2c = busio.I2C(board.SCL, board.SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128,64,i2c)

disp.fill(1)
disp.show()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height),outline=0,fill=1)

#image = Image.open('opn.ppm').convert('1')
#image = image.resize((width,height))
counter = 12
direction = -1
while True:
    draw.ellipse((4, 40-counter, 54, 40+counter), outline=0, fill=1)
    draw.ellipse((74, 40-counter, 124, 40+counter), outline=0, fill=1)
    draw.ellipse((19, 32, 39, 48), outline=0, fill=0)
    draw.ellipse((89, 32, 109, 48), outline=0, fill=0)
    disp.image(image)
    disp.show()

    if counter > 12:
        direction = -1
    if counter < 1:
        direction = +1

    counter = counter + direction
    #print("Hello")


