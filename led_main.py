# Author: David J. Glowny
# Last Edited: 05/30/2017

import sys
from image_functions import *
from led_strand_functions import *

if __name__ == '__main__':


	if len(sys.argv) != 2:

		print "ERROR: Invalid arguments"
		print "USAGE: python led_main/py <image file>"

	else:

		try:

			in_image = Image(sys.argv[1])

			old_color = find_random_color(in_image)

			# Create NeoPixel object with appropriate configuration.
			strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
			# Intialize the library (must be called once before other functions).
			strip.begin()
			
			#make leds less bright
			strip.setBrightness(220)

			print ('Press Ctrl-C to quit.')

			#display starting color
			colorAppear(strip, old_color)

			while True:

				#find next color randomly from popular colors in image
				new_color = find_random_color(in_image)
				
				print "New Color"
				print new_color
				
				#apply new color to LEDs
				fade_to_new_color(strip, old_color, new_color)
				old_color = new_color

		except KeyboardInterrupt:

			#turn off LEDs
			colorWipe(strip, Color(0, 0, 0))

			sys.exit(0)