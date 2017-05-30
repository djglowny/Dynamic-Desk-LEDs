# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def colorAppear(strip, color, wait_ms=50):
	
	proper_color = Color(color[0], color[1], color[2])
	
	"""Show color across display at once."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, proper_color)
	strip.show()
	time.sleep(wait_ms/1000.0)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def increment_color(old_rgb, new_rgb):
	
	
	"""Make small changes in old color to closer match new color"""
	#move value of red one step closer to new value
	if new_rgb[0] > old_rgb[0]:
		old_rgb = ( (old_rgb[0]+1), old_rgb[1], old_rgb[2] )
		
	elif new_rgb[0] < old_rgb[0]:
		old_rgb = ( (old_rgb[0]-1), old_rgb[1], old_rgb[2] )
		
	#move value of blue one step closer to new value
	if new_rgb[1] > old_rgb[1]:
		old_rgb = ( old_rgb[0], (old_rgb[1]+1), old_rgb[2] )

	elif new_rgb[1] < old_rgb[1]:
		old_rgb = ( old_rgb[0], (old_rgb[1]-1), old_rgb[2] )

	#move value of green one step closer to new value
	if new_rgb[2] > old_rgb[2]:
		old_rgb = ( old_rgb[0], old_rgb[1], (old_rgb[2]+1) )
		
	elif new_rgb[2] < old_rgb[2]:
		old_rgb = ( old_rgb[0], old_rgb[1], (old_rgb[2]-1) )
		

	return old_rgb


def fade_to_new_color(strip, old_rgb, new_rgb, wait_ms=200):
	"""Slowly transition to new rgb value across all pixels"""
	
	while cmp(old_rgb, new_rgb) != 0:
		
		print "OLD RGB:"
		print old_rgb
		print "NEW RGB:"
		print new_rgb
		
		old_rgb = increment_color(old_rgb, new_rgb)
		
		for i in range(strip.numPixels()):
			
			proper_color = Color(old_rgb[0], old_rgb[1], old_rgb[2])
			
			strip.setPixelColor(i, proper_color)
		strip.show()
		time.sleep(wait_ms/1000.0)

	#else, just sleep
	time.sleep(wait_ms/1000.0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)