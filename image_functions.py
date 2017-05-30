# Author: David J. Glowny
# Last Edited: 05/30/2017

import random
from SimpleCV import *

def grab_image_file(file_str):
	
	my_image = Image(file_str)
	return my_image

def custom_findBlobs(my_image):

	#based on documentation (http://simplecv.sourceforge.net/doc/SimpleCV.html):
	threshval=-1
	minsize=10
	maxsize=0
	threshblocksize=0
	threshconstant=5

	#list of blobs is already sorted by size
	return my_image.findBlobs(threshval,minsize,maxsize,threshblocksize,threshconstant)

def find_random_color(my_image):
	#select a random color from the spectrum of major colors from the image
	key_blobs = custom_findBlobs(my_image)
	selected_color = random.choice(key_blobs).meanColor()
	
	print "Selected Color:"
	print (int(selected_color[0]), int(selected_color[1]), int(selected_color[2]))

	#convert rgb values to integers
	return (int(selected_color[0]), int(selected_color[1]), int(selected_color[2]))
