# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 00:40:49 2018

@author: MorpheusChang
"""
from PIL import Image

def blur(img, radius):
    dst = img
    surface = (radius * 2) ** 2
    for x in range(radius, img.width - radius):
        for y in range(radius, img.height - radius):
            r = 0
            g = 0
            b = 0
            for rectY in range(y - radius, y + radius):
                for rectX in range(x - radius, x + radius):
                    pixel = img.getpixel((rectX, rectY))
                    r += pixel[0]
                    g += pixel[1]
                    b += pixel[2]
            dst.putpixel((x, y), (r // surface, g // surface, b // surface))
        print(int((x - radius) / (img.width - 1 - radius*2) * 100), "%", end="\r")

def blurAngle(img, radius):
    dst = img
    surface = (radius * 2) ** 2
    for x in range(img.width):
        for y in range(img.height):
            r = 0
            g = 0
            b = 0
            for rectY in range(y - radius, y + radius):
                for rectX in range(x - radius, x + radius):
                    if rectX < 0:
                        rectX = 0
                    elif rectX >= img.width:
                        rectX = img.width - 1
                    if rectY < 0:
                        rectY = 0
                    elif rectY >= img.height:
                        rectY = img.height - 1
                    pixel = img.getpixel((rectX, rectY))
                    r += pixel[0]
                    g += pixel[1]
                    b += pixel[2]
            dst.putpixel((x, y), (r // surface, g // surface, b // surface))
        print(int(x / img.width * 100), "%", end="\r")
    print("100 %")
    return dst

def bigger(img, factor):
    new = Image.new("RGB", (img.width * factor, img.height * factor))
    for x in range(img.width):
        for y in range(img.height):
            for yB in range(factor):
                for xB in range(factor):
                    new.putpixel((x * factor + xB, y * factor + yB), img.getpixel((x, y)))
    return new

def smaller(img, factor):
    new = Image.new("RGB", (img.width // factor, img.height // factor))
    for x in range(0, img.width // factor):
        for y in range(0, img.height // factor):
            new.putpixel((x, y), img.getpixel((x * factor, y * factor)))
    return new

def quickBlur(img, radius):
    dst = img.copy()
    surface = (radius * 2)
    for x in range(radius, img.width - radius):
        for y in range(radius, img.height - radius):
            r = 0
            g = 0
            b = 0
            for rectY in range(y - radius, y + radius):
                pixel = img.getpixel((x, rectY))
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
            dst.putpixel((x, y), (r // surface, g // surface, b // surface))
        print(int((x - radius) / (img.width - radius*2) * 50), "%", end="\r")
    img = dst.copy()
    for x in range(radius, img.width - radius):
        for y in range(radius, img.height - radius):
            r = 0
            g = 0
            b = 0
            for rectX in range(x - radius, x + radius):
                pixel = dst.getpixel((rectX, y))
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
            img.putpixel((x, y), (r // surface, g // surface, b // surface))
        print(int((x - radius) / (img.width - radius*2) * 50 + 50), "%", end="\r")
    print("100 %")
    return img

def quickBlurAngle(img, radius):
    dst = img.copy()
    surface = (radius * 2)
    for x in range(img.width):
        for y in range(img.height):
            r = 0
            g = 0
            b = 0
            for rectY in range(y - radius, y + radius):
                if rectY < 0:
                    rectY = 0
                elif rectY >= img.height:
                    rectY = img.height - 1
                pixel = img.getpixel((x, rectY))
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
            dst.putpixel((x, y), (r // surface, g // surface, b // surface))
        print(int(x / img.width * 50), "%", end="\r")
    img = dst.copy()
    for x in range(img.width):
        for y in range(img.height):
            r = 0
            g = 0
            b = 0
            for rectX in range(x - radius, x + radius):
                if rectX < 0:
                    rectX = 0
                elif rectX >= img.width:
                    rectX = img.width - 1
                pixel = dst.getpixel((rectX, y))
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
            img.putpixel((x, y), (r // surface, g // surface, b // surface))
        print(int(x / img.width * 50 + 50), "%", end="\r")
    print("100 %")
    return img
"""
img = Image.open("wikipedia.jpg")
img = smaller(img, 8)
img = quickBlurAngle(img, 4)
img = quickBlurAngle(img, 4)
img = bigger(img, 4)
img = quickBlurAngle(img, 2)
img = bigger(img, 2)
img.show()
"""
img = Image.open("wikipedia.jpg")
img = blurAngle(img, 8)
img.show()
