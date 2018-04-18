# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 18:13:22 2018

@author: nicholaschang
"""
# 

import cv2
import numpy as np

def conv_transform(img):
    image_copy = img.copy()
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            image_copy[i][j] = img[img.shape[0]-i-1][img.shape[1]-j-1]
    return image_copy

def conv(img, kernel):
    kernel = conv_transform(kernel)
    img_h =img.shape[0]
    img_w =img.shape[1]
    
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]
    
    h = kernel_h//2
    w = kernel_w//2
    
    img_conv =np.zeros(img.shape)
    
    for i in range(h, img_h-h):
        for j in range(w, img_w-w):
            sum = 0
            
            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum = sum + kernel[m][n]*img[i-h+m][j-w+n]
            img_conv[i][j] = sum
    return img_conv
  
def norm(img1,img2):
   img_copy = np.zeros(img1.shape) #image with initial zero values
   #img_copy - img1.copy()
   
   for i in range(img1.shape[0]):
       for j in range(img1.shape[1]):
           q = (img1[i][j]**2 + img2[i][j]**2)**(1/2)
           if (q>90):   #threshold
               img_copy[i][j] = 255  #obtain binary image
           else:
               img_copy[i][j] = 0            
   return img_copy            


def opencv_sobel(img):
    img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    img_gaussian =  cv2.GaussianBlur(img_gray,(3,3),0)  #let Kernel = 3 * 3
    #sobel
    img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
    img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
    img_sobel = img_sobelx + img_sobely
    
    cv2.imshow("Sobel Edge detector Using openCV", img_sobel)
    cv2.waitKey(0)
    

def opencv_gaussianblur(img):
    gausBlur = cv2.GaussianBlur(img, (5,5),0)   #let kernel = 5 * 5
    cv2.imshow('Gaussian Blur image Using openCV', gausBlur)
    cv2.waitKey(0)

def opencv_dilation(img):
    kernel = np.ones((5,5), np.uint8)
    img_dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imshow('Dilation', img_dilation)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    
    img = cv2.imread("wiki.png")
    opencv_sobel(img)          #sobel edge using opencv
    opencv_gaussianblur(img)    #gaussianblur using opencv
    opencv_dilation(img)
    
   #Gx ,Gy for sobel_operator on wiki
    
    kernel = np.zeros(shape=(3,3))
    kernel[0, 0] = -1
    kernel[0, 1] = -2
    kernel[0, 2] = -1
    
    kernel[1, 0] =  0
    kernel[1, 1] =  0
    kernel[1, 2] =  0
    
    kernel[2, 0] =  1
    kernel[2, 1] =  2
    kernel[2, 2] =  1
    
    print(kernel[2][0])
    gradient_y = conv(img, kernel)
    #cv2.imshow("gradient_y",gradient_y)
    #cv2.waitKey(0)
    
    kernel[0, 0] = -1
    kernel[0, 1] =  0
    kernel[0, 2] =  1
    
    kernel[1, 0] =  -1
    kernel[1, 1] =  0
    kernel[1, 2] =  1
    
    kernel[2, 0] =  -2
    kernel[2, 1] =  0
    kernel[2, 2] =  2
    
    gradient_x = conv(img, kernel)
    #cv2.imshow("gradient_x", gradient_x)
    #cv2.waitKey(0)
    

    
    sobel_edge = norm(gradient_x, gradient_y)
    cv2.imshow("sobel edge without opencv",sobel_edge)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()