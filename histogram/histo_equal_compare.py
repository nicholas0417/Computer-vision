import pylab as plt	                # matplotlib's subpackage as plt for graph
import numpy as np	                # use numpy library as np for array object
import cv2			                # opencv-python

def Hist_Equal(image):				# define function histogram equalization (input image)
### count values for each pixels
	x, y = image.shape 				# get image size x*y, for a image with x rows and y columns
	histo = [0.0] * 256 			# Initializes a 256 array to hold the number of
									# occurrences of each gray level
	for i in range(0, x): 			# count each pixel value(gray level) from 0 to x
		for j in range(0, y): 		# count each pixel value(gray level) from 0 to y
			histo[image[i, j]]+=1	# count the number of occurrences of each gray level

### cdf and new pixels values

	cdf = np.cumsum(np.array(histo))						# cumulative distribution function
	trans_val = np.uint8((cdf-cdf[0])/((x*y)-cdf[0])*255)	# calculate transfer value

### applying transfered values for each pixels

	new_img = np.zeros_like(image) 	                         # Return an empty array new_img with shape and type of input.
	for i in range(0, x):			                         # count each pixel value(gray level) from 0 to x
		for j in range(0, y):		                         # count each pixel value(gray level) from 0 to y
			new_img[i, j] = trans_val[image[i, j]]	         # fill the equalization result in the array

	return new_img					                         # return transformed image
