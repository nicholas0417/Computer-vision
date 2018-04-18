# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:00:18 2018

@author: MorpheusChang
"""

import cv2
import numpy as np

num_down = 2
num_bilateral =7
# load our input image
img_rgb = cv2.imread('s1030340.jpg')


# downsample image using Gaussian pyramid
img_color = img_rgb
for _ in range(num_down):
    img_color = cv2.pyrDown(img_color)

# repeatedly apply small bilateral filter instead of
# applying one large filter
for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9,
                                    sigmaColor=9,
                                    sigmaSpace=7)
# upsample image to original size
for _ in range(num_down):
    img_color = cv2.pyrUp(img_color)

"""
OpenCV offers a variety of choices when it comes to edge detection.
The beauty of adaptive thresholding is that it detects the most salient features
in each (small) neighborhood of an image, independent of the overall properties
of the image, which is exactly what we want when we seek to draw bold,
black outlines around objects and people in a cartoon.
However, this property also makes adaptive thresholding susceptible to noise.
It is therefor a good idea to pre-process the image with a median filter, which
replaces each pixel value with the median value of all the pixels in a small
(e.g., 7 pixel) neighborhood:
"""
# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Takes median of all the pixels under kernel area and central
# element is replaced with this median value
median = cv2.medianBlur(gray_image, 7)

img_edge = cv2.adaptiveThreshold(median, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,
                                 blockSize=9,
                                 C=2)
cv2.imshow('original', img_rgb)
cv2.waitKey(0)
#Python: cv2.bitwise_and(src1, src2[, dst[, mask]])
"""
Parameters:
src1 – first input array or a scalar.
src2 – second input array or a scalar.
src – single input array.
value – scalar value.
dst – output array that has the same size and type as the input arrays.
mask – optional operation mask, 8-bit single channel array, that specifies elements of the output array to be changed.

"""
color_img = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
cart_img = cv2.bitwise_and(color_img,img_rgb)

cv2.imshow('Cartoon', cart_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
