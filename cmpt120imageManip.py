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
def invert(pixels) :
  width = len(pixels)
  height = len(pixels[0])

  # invert each pixel by subtracting 255 from the color value and taking the
  # absolute value of it
  for i in range(width) :
    for j in range(height) :
      for k in range(3) :
        pixels[i][j][k] = abs(pixels[i][j][k] - 255)
  return pixels

def flipHorizontal(pixels) :
  width = len(pixels)
  height = len(pixels[0])
  halfWidth = int(width / 2)

  # For each column from left edge to the center of the image, swap each pixel
  # with the one on the opposite side horizontally (-i)
  for i in range(halfWidth) :
    for j in range(height) :
      temp = pixels[i][j]
      pixels[i][j] = pixels[-i][j]
      pixels[-i][j] = temp
  return pixels

def flipVertical(pixels) :
  width = len(pixels)
  height = len(pixels[0])
  halfHeight = int(height / 2)

  # For each column from left edge to the center of the image, swap each pixel
  # with the one on the opposite side vertically (-i)
  for i in range(width) :
    for j in range(halfHeight) :
      temp = pixels[i][j]
      pixels[i][j] = pixels[i][-j]
      pixels[i][-j] = temp
  return pixels


###                        ###
### Intermediate functions ###
###                        ###
def removeRedChannel(pixels) :
    return pixels

def removeGreenChannel(pixels) :
    return pixels

def removeBlueChannel(pixels) :
    return pixels

def convertToGreyscale(pixels) :
    return pixels

def applySepiaFilter(pixels) :
    return pixels

def decreaseBrightness(pixels) :
    return pixels

def increaseBrightness(pixels) :
    return pixels

###                    ###
### Advanced functions ###
###                    ###
def rotateLeft(pixels) :
    return pixels

def rotateRight(pixels) :
    return pixels

def pixelate(pixels) :
    return pixels

def binarize(pixels) :
    return pixels
