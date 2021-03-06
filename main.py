# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Connor Goudie, Oliver Lin
# Date: Dec 7, 2020
# Description: Driver for a program that can open an image, edit it in some way, and be saved
# this file generates the UI, loads the image, and allows the user to input instructions to
# edit an opened image in some way. List of manipulations and their code is in cmpt120imagemanip.py

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
        "Q: Quit",
        "O: Open Image",
        "S: Save current image",
        "R: Reload original image"
         ]

# list of basic operation options
basic = [        
        "1: Switch to Intermeidate Functions",
        "2: Switch to Advanced Functions",
        "3: Invert",
        "4: Flip Horizontal",
        "5: Flip Vertical"
         ]

# list of intermediate operation options
intermediate = [                 
        "1: Switch to Basic Functions",
        "2: Switch to Advanced Functions",
        "3: Remove red",
        "4: Remove green",
        "5: Remove blue",
        "6: Convert to grayscale",
        "7: Apply sepia filter",
        "8: Decrease brightness",
        "9: Increase brightness"
        ]

# list of advanced operation options
advanced = [
        "1: Switch to Basic Functions",
        "2: Switch to Intermediate Functions",
        "3: Rotate left",
        "4: Rotate right",
        "5: Pixelate",
        "6: Binarize"
         ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-5)")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-9)")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)")
    else:
        menuString.append("Error: Unknown mode!")
    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    titleString = ""
    openFilename = ""
    # removes the full path name of the file, leaving only the file name
    openFilenameCondensed = appStateValues["lastOpenFilename"].split("/")[-1]
    
    userInput = state["lastUserInput"].upper()
    
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "O":
          tkinter.Tk().withdraw()
          openFilename = tkinter.filedialog.askopenfilename()
          if openFilename!= "":
              img = cmpt120imageProj.getImage(openFilename)
              appStateValues["lastOpenFilename"] = openFilename
              titleString = "Opened "
          else:
              print("Error: no file opened")
              
        elif userInput == "S":
          tkinter.Tk().withdraw()
          saveFilename = tkinter.filedialog.asksaveasfilename()
          if saveFilename != "":
              cmpt120imageProj.saveImage(img, saveFilename)
              appStateValues["lastSaveFilename"] = saveFilename
              titleString = "Saved "
          else:
              print("Error: no file saved")
              
        elif userInput == "R":
          openFilename = appStateValues["lastOpenFilename"]
          if openFilename != "" :
              img = cmpt120imageProj.getImage(openFilename)
              titleString = "Reloaded "
          else:
              titleString = "No Image "
              print("Error: no file to reload")

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # Basic mode
        if appStateValues["mode"] == "basic":
          if int(userInput) == 1:
            appStateValues["mode"] = "intermediate"
            titleString = "Intermediate mode "
          elif int(userInput) == 2:
            appStateValues["mode"] = "advanced"
            titleString = "Advanced mode "
          elif int(userInput) == 3:
            cmpt120imageManip.invert(img)
            titleString = "Invert "
          elif int(userInput) == 4:
            cmpt120imageManip.flipHorizontal(img)
            titleString = "Flip horizontal "
          elif int(userInput) == 5:
            cmpt120imageManip.flipVertical(img)
            titleString = "Flip vertical "
        # Intermediate mode
        elif appStateValues["mode"] == "intermediate":
          if int(userInput) == 1:
            appStateValues["mode"] = "basic"
            titleString = "Basic mode "
          elif int(userInput) == 2:
            appStateValues["mode"] = "advanced"
            titleString = "Advanced mode "
          elif int(userInput) == 3:
            cmpt120imageManip.removeRedChannel(img)
            titleString = "Invert "
          elif int(userInput) == 4:
            cmpt120imageManip.removeGreenChannel(img)
            titleString = "Remove green channel "
          elif int(userInput) == 5:
            cmpt120imageManip.removeBlueChannel(img)
            titleString = "Remove blue channel "
          elif int(userInput) == 6:
            cmpt120imageManip.convertToGreyscale(img)
            titleString = "Grayscale "
          elif int(userInput) == 7:
            cmpt120imageManip.applySepiaFilter(img)
            titleString = "Apply sepia filter "
          elif int(userInput) == 8:
            cmpt120imageManip.decreaseBrightness(img)
            titleString = "Decrease brightness "
          elif int(userInput) == 9:
            cmpt120imageManip.increaseBrightness(img)
            titleString = "Increase brightness "
        # Advanced mode
        elif appStateValues["mode"] == "advanced":
          if int(userInput) == 1:
            appStateValues["mode"] = "basic"
            titleString = "Basic mode "
          elif int(userInput) == 2:
            appStateValues["mode"] = "intermediate"
            titleString = "Intermediate mode "
          elif int(userInput) == 3:
            img = cmpt120imageManip.rotateLeft(img)
            titleString = "Rotate left "
          elif int(userInput) == 4:
            img = cmpt120imageManip.rotateRight(img)
            titleString = "Rotate right "
          elif int(userInput) == 5:
            cmpt120imageManip.pixelate(img)
            titleString = "Pixelate "
          elif int(userInput) == 6:
            cmpt120imageManip.binarize(img)
            titleString = "Binarize "
    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
        
    # if a file was opened change the title, otherwise use the default (openFilenameCondensed)
    if openFilename == "" :
        titleString += openFilenameCondensed
    else:
        titleString += openFilename.split("/")[-1]
        
    cmpt120imageProj.showInterface(img, titleString, generateMenu(appStateValues))
    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
