# Author : Honorio Vega
# Purpose : Read a series of pictures and remove an obstruction
#           by applying a median filter to each pixel for each picture
# GITHUB LINK : https://github.com/honoriovega/CST205-proj1-hvega.git
from PIL import Image
import glob

# compute median of odd number of items in list
def medianOdd(a) : return sorted(a)[len(a) // 2]

# compute median of even number of items in list
def medianEven(a):
    a.sort()
    mid = len(a) // 2
    return (a[mid] + a[mid - 1]) // 2

# load the images given the path name
def loadImages(path):
    return [ Image.open(file) for file in glob.glob('%s/*' % path) ]

def main():

    # load the images
    pics = loadImages('Project1Images')

    # store the dimensions
    pictureWidth, pictureHeight = pics[0].size

    # pick the appropriate median function based on number
    # of pictures
    median = medianEven if len(pics) % 2 == 0 else medianOdd

    # open a blank file to write to
    result = Image.new('RGB', (pictureWidth, pictureHeight) )

    r_list = []
    g_list = []
    b_list = []

    # perform the calculation
    for x in range(pictureWidth):
        for y in range(pictureHeight) :
            for pic in pics:
                r, g, b = pic.getpixel( (x,y ) )
                r_list.append(r)
                g_list.append(g)
                b_list.append(b)

            result.putpixel( (x,y), ( median(r_list),
                                   median(g_list),
                                   median(b_list) )
                        )

            r_list = []
            g_list = []
            b_list = []

    result.save('manRemoved.png')

main()