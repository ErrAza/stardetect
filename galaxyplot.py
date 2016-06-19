from PIL import Image
from pylab import *
from pylab import plot
from datetime import datetime
import uuid
import os

coordinates = []


def main(argv):
    if (len(argv) == 1) or (argv[1] == "help"):
        print "Usage: python galaxyplot (1)InputImage (2)OutputImage"
        return

    red = (255, 0, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    intensity = 250
    pixleTolerance = 10
    pixelStrength = 250
    redPixels = 0
    bluePixels = 0
    isRed = False
    isBlue = False
    xaxis = 0
    yaxis = 0
    possibleGalaxies = 0
    im = Image.open(argv[1])
    outputFile = argv[2]
    print im.size
    xaxis = im.size[0]
    yaxis = im.size[1]
    
    print "Busy..."
    rgb_im = im.convert('RGB')
    pix = im.load()
    for x in range(xaxis):
        for y in range(yaxis):
            r, g, b = rgb_im.getpixel((x, y))
            if r >= intensity:
                bluePixels = 0
                if isRed:
                    redPixels = redPixels + 1
                if redPixels > pixleTolerance:
                    pix[x, y] = red
                isRed = True
                isBlue = False
                if redPixels >= pixelStrength:
                    possibleGalaxies = possibleGalaxies + 1
                    pos = (x, y)
                    saveposition(pos)
            elif b >= intensity:
                redPixels = 0
                if isBlue:
                    bluePixels = bluePixels + 1
                if bluePixels > pixleTolerance:
                    pix[x, y] = blue
                isBlue = True
                isRed = False
                if bluePixels >= pixelStrength:
                    possibleGalaxies = possibleGalaxies + 1
                    pos = (x, y)
                    saveposition(pos)
            else:
                pix[x, y] = black
    plotcoords(coordinates)
    
    print "Plotting coordinates..."
    writetxt(coordinates)
    print "Log created at" + os.getcwd()
    print "Saving image..."
    im.save(outputFile)

    print "Displaying figure..."
    unique_imagename = str(uuid.uuid4())
    plt.savefig(unique_imagename + ".jpg")
    show()

def saveposition(pos):
    coordinates.append(pos)


def plotcoords(coordinates):
    for (x, y) in coordinates:
        plot(x, y, '+')


def writetxt(coordinates):
    unique_filename = str(uuid.uuid4())
    filename = os.getcwd() + unique_filename + ".log"
    text_file = open(filename, "w")
    for position in coordinates:
        text_file.write(str(position) + '\n')
    text_file.close




if __name__ == "__main__":
    main(sys.argv)
