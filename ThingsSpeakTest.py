#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  temp_thingspeak solution.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#import sys
#import RPi.GPIO as GPIO
from time import sleep
#import Adafruit.DHT
import urllib2
import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=40)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Load default font.
font = ImageFont.load_default()
fontMinecraft = ImageFont.truetype('minecraft.ttf', 14)
# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
'''
def getSensorData():
	RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
	return (str(RH), str(T))
'''
def updateScreen(temp, humidity):
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	disp.clear()
	disp.display()
	draw.text((0,6), 'TEMP', font = fontMinecraft)
	draw.text((50,6), str(temp), font = fontMinecraft)
	draw.text((0,30), 'HUMI', font = fontMinecraft)
	draw.text((50,30), str(humidity), font = fontMinecraft)
	disp.image(image)
	disp.display()
	return

def main():
	api_key = 'F73UJO8TFQS7TP8X'
	baseURL = 'https://api.thingspeak.com/update?api_key=%s' % api_key
	number1 = 1
	number2 = 2
	



	
	while True:
		try:
			#RH, T = getSensorData()
			number1 += 1
			number2 += 2
			f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (number1, number2))
			print f.read()
			print 'Number1 =', number1
			print 'Number2 =', number2
			f.close()
			updateScreen(number1, number2)
			#draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
			#disp.clear()
			#disp.display()
			#draw.text((10,30), str(number1), font = font)
			#disp.image(image)
			#disp.display()
			sleep(15)
		except:
			print 'exiting'
			break
	return 0
			
			
# Call main
if __name__ == '__main__':
	main()











































