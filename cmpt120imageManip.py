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
    width = len(img)
    height = len(img[0])
    
    # sets red value to 0 for all pixels in the image
    for i in range(width) :
        for j in range(height) :
            img[i][j][0] = 0
    return img

def removeGreenChannel(img) :
    width = len(img)
    height = len(img[0])
    
    # sets green value to 0 for all pixels in the image
    for i in range(width) :
        for j in range(height) :
            img[i][j][1] = 0
    return img

def removeBlueChannel(img) :
    width = len(img)
    height = len(img[0])
    
    # sets blue value to 0 for all pixels in the image
    for i in range(width) :
        for j in range(height) :
            img[i][j][2] = 0
    return img

def convertToGreyscale(img) :
    width = len(img)
    height = len(img[0])
    
    for i in range(width) :
        for j in range(height) :
            totalColourVal = 0
            # sum the total of all colour values, then average them
            for k in range(3) :
                totalColourVal += img[i][j][k]
            average = totalColourVal / 3
            
            # set each colour value to the average
            for k in range(3) :
                img[i][j][k] = average
    return img
  
def applySepiaFilter(img) :
    img = convertToGreyscale(img)
    width = len(img)
    height = len(img[0])

    for i in range(width) :
        for j in range(height) :
            sepiaRed = int((img[i][j][0] * .393) + (img[i][j][1] * .769)
                           + (img[i][j][2] * .189))
            sepiaGreen = int((img[i][j][0] * .349) + (img[i][j][1] * .686)
                             + (img[i][j][2] * .168))
            sepiaBlue = int((img[i][j][0] * .272) + (img[i][j][1] * .534)
                            + (img[i][j][2] * .131))
            
            if sepiaRed > 255 : sepiaRed = 255
            if sepiaGreen > 255 : sepiaGreen = 255
            if sepiaBlue > 255 : sepiaBlue = 255

            img[i][j][0] = sepiaRed
            img[i][j][1] = sepiaGreen
            img[i][j][2] = sepiaBlue
    return img

def decreaseBrightness(img) :
    return img

def increaseBrightness(img) :
    return img

###                    ###
### Advanced functions ###
###                    ###
def rotateLeft(img) :
    width = len(img)
    height = len(img[0])

    # create a new empty array
    newImg = []
    for i in range(height) :
        newImg.append([])
        for j in range(width) :
            newImg[i].append([])
            for k in range(3) :
              newImg[i][j].append(0)

    # copy the first row of pixels, because of using -i in the next loop, the
    # first row does not copy
    print(len(newImg[0]))
    print(width)
    for i in range(height) :
        for k in range(3) :
            newImg[i][width - 1][k] = img[i][0][k]

    # copy the old pixels into the new image from the second row onwards      
    for i in range(1, width) :
        for j in range(1, height) :
            for k in range(3) :
                newImg[j][-i][k] = img[i][j][k]
    return newImg

def pixelate(img) :
    width = len(img)
    height = len(img[0])
    # Ignores edge pixels if image dimensions not divisible by 4
    width -= width % 4
    height -= height % 4
    
    # For every 4x4 block of pixels
    for i in range(0, width, 4) :
        for j in range(0, height, 4) :
            # Get the total RGB values of the block
            redTotal = 0
            greenTotal = 0
            blueTotal = 0
            for x in range(i, i + 4) :
                for y in range(j, j + 4) :
                    redTotal += img[x][y][0]
                    greenTotal += img[x][y][1]
                    blueTotal += img[x][y][2]
            # Average the RGB totals and replace pixels with the averages
            redAverage = redTotal / 16
            greenAverage = greenTotal / 16
            blueAverage = blueTotal / 16
            for x in range(i, i + 4) :
                for y in range(j, j + 4) :
                    img[x][y][0] = redAverage
                    img[x][y][1] = greenAverage
                    img[x][y][2] = blueAverage
    return img

def rotateRight(img) :
    return img

def binarize(img) :
    return img
