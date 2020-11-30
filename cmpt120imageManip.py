# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s):
# Date:
# Description:

import cmpt120imageProj
import numpy

###                 ###
### Basic functions ###
###                 ###
def invert(img) :
  width = len(img)
  height = len(img[0])

  # invert each pixel by subtracting 255 from the color value and taking the
  # absolute value of it
  for i in range(width) :
    for j in range(height) :
      for k in range(3) :
        img[i][j][k] = abs(img[i][j][k] - 255)
  return img

def flipHorizontal(img) :
  width = len(img)
  height = len(img[0])
  halfWidth = int(width / 2)

  # For each column from left edge to the center of the image, swap each pixel
  # with the one on the opposite side horizontally (-i)
  for i in range(halfWidth) :
    for j in range(height) :
      temp = img[i][j]
      img[i][j] = img[-i][j]
      img[-i][j] = temp
  return img

def flipVertical(img) :
  width = len(img)
  height = len(img[0])
  halfHeight = int(height / 2)

  # For each row from left edge to the center of the image, swap each pixel
  # with the one on the opposite side vertically (-j)
  for i in range(width) :
    for j in range(halfHeight) :
      temp = img[i][j]
      img[i][j] = img[i][-j]
      img[i][-j] = temp
  return img


###                        ###
### Intermediate functions ###
###                        ###
def removeRedChannel(img) :
    return img

def removeGreenChannel(img) :
    return img

def removeBlueChannel(img) :
    return img

def convertToGreyscale(img) :
    return img

def applySepiaFilter(img) :
    return img

def decreaseBrightness(img) :
    return img

def increaseBrightness(img) :
    return img

###                    ###
### Advanced functions ###
###                    ###
def rotateLeft(img) :
    return img

def rotateRight(img) :
    return img

def pixelate(img) :
    return img

def binarize(img) :
    return img
