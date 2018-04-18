import pylab as plt	# matplotlib's subpackage as pl for graph
import numpy as np	# use numpy library as np for array object
import cv2			# opencv-python

def histo(image):
	x, y = image.shape 				# get image size x*y, for a image with x rows and y columns
	histo = [0.0] * 256 			# Initializes a 256 array to hold the number of
									# occurrences of each gray level
	for i in range(0, x): 			# count each pixel value(gray level) from 0 to x
		for j in range(0, y): 		# count each pixel value(gray level) from 0 to y
			histo[image[i, j]]+=1	# count the number of occurrences of each gray level

	return np.array(histo)			# return histogram

img = cv2.imread('2012_003523.jpg') # read image

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert image to grayscal
original_histo = histo(grayimg)				   # calculate original image's histogram

from histo_equal_compare import Hist_Equal     # use histogram equalization algorithm
new_img = Hist_Equal(grayimg)			       # histogram equalized image
new_histo = histo(new_img)				       # new image's histogram

openCV_img = cv2.equalizeHist(grayimg)         # openCV function histogram equalization
openCV_histo = histo(openCV_img)	           # opencv function's result histogram


plt.subplot(231)					# image position 2 row, 3 column, first position
plt.imshow(grayimg)				    # show image "grayimg"
plt.title('original image')		    # graph title "original image"
plt.set_cmap('gray')				# show in gray scale

plt.subplot(232)					# image position 2 row, 3 column, second position
plt.imshow(new_img)				    # show image "new_img"
plt.title('equalized image')		# graph title "equalized image"
plt.set_cmap('gray')				# show in gray scale

plt.subplot(233)					# image position 2 row, 3 column, third position
plt.imshow(openCV_img)			    # show image "openCV_img"
plt.title('openCV equalized image')	# graph title "openCV equalized image"
plt.set_cmap('gray')				# show in gray scale

plt.subplot(234)					# image position 2 row, 3 column, fourth position
plt.plot(original_histo)			# show image "original_histo"
plt.title('Original histogram')	    # graph title "original histogram"

plt.subplot(235)					# image position 2 row, 3 column, fifth position
plt.plot(new_histo)				    # show image "new_histo"
plt.title('equalized histogram') 	# graph title "New histogram"

plt.subplot(236)					# image position 2 row, 3 column, sixth position
plt.plot(openCV_histo)			    # show image "openCV_histo"
plt.title('openCV equalized histogram')	# graph title "openCV histogram"

plt.show()
