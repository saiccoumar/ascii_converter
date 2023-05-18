# http://www.jave.de/image2ascii/algorithms.html
# https://aa-project.sourceforge.net/aalib/
# https://github.com/JEphron/TEXTFLIX/blob/master/main.py

import sys, random, argparse
import numpy as np
import math
import os
from PIL import Image, ImageEnhance



os.system("color")

def convert_blackwhite(img, factor, save):
# Function Convert Image to text
# 0: Tuples that map all 16 possible combinations of pixels to an ASCII character
    black_white_chars = {
    # Format of [(x1,y1),(x2,y1),(x1,y2),(x2,y2)]
        (False, False, False, False) : ' ', #0 
        (False, True, False, False) : '.', #1
        (True, False, False, False) : ',', #1
        (False, False, True, False) : '\'', #1
        (False, False, False, True) : '_', #1
        (True, True, False, False) : '+', #2 
        (False, False, True, True) : '*', #2 
        (True, False, True, False) : ';', #2
        (False, True, False, True) : ':', #2
        (False, True, True, False) : '=', #2
        (True, False, False, True) : '[', #2
        (False, True, True, True) : ']', #3
        (True, True, False, True) : 'J', #3
        (True, False, True, True): 'I', #3 
        (True, True, True, False) : '0', #3
        (True, True, True, True) : '@' #4
    }
# 1: Resize image.
    width, height = img.size
    scale = width / (factor*100)
    width, height = width / scale, height / (scale*2)
    
    img = img.resize((int(width), int(height)), Image.ANTIALIAS)
# 2: Enhance image for better output
    img = ImageEnhance.Sharpness(img).enhance(5)
    img = ImageEnhance.Contrast(img).enhance(1.5)
# 3: Turn image into array of numbers and convert image to greyscale    
    img_array_grey = np.array(img.convert("1")) #Uses black/white 
# 4: Iterate through every 4 pixels and convert it into an ascii character and append ascii character to string
    str = ""
    for li in range(0,math.floor(len(img_array_grey) / 2) * 2,2): #Floor function to use only even bounds. 
        #Odd bounds have data loss on last col/row
        for i in range(0,math.floor(len(img_array_grey[li]) / 2.) * 2,2):
            tu = (img_array_grey[li, i],img_array_grey[li+1, i],img_array_grey[li, i+1],img_array_grey[li+1, i+1])
            str = str + black_white_chars[tu]
        str = str + '\n'
# 5: Output to terminal
    print(str)
# 6: Save to output file
    if(save):
        with open('output.txt','w') as f:
            f.write(str)


def convert_grey(img, color, factor, save):
    grey_ramp = ' .\'`^",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
    # grey_ramp = '@%#*+=-:.'
    # grey_ramp = grey_ramp[::-1]
    # print(grey_ramp)
    width, height = img.size
    scale = width / (factor*100)
    width, height = width / scale, height / (scale*2)
    img = img.resize((int(width), int(height)), Image.ANTIALIAS)
# 2: Enhance image for better output
    img = ImageEnhance.Sharpness(img).enhance(5)
    img = ImageEnhance.Contrast(img).enhance(1.5)
# 3: Turn image into array of numbers and convert image to greyscale    
    # img_array_grey = np.array(img.convert("L")) #Uses greyscaling
    img_array = np.array(img)
    img_array_grey = np.array(img.convert("L"))
# 4: Mapping greyscaled value to the grey_ramp
    def map(x):
        return (math.floor(x * len(grey_ramp) / 255) - 1)
# 5: Iterate through every value and print append corresponding character to string
    str = ""
    for li in range(0,len(img_array_grey)):
        for i in range(0,len(img_array_grey[li])):
            # Conditional to either print in color or not 
            if(color):
                str = str + rgb(img_array[li][i][0],img_array[li][i][1],img_array[li][i][2]) + grey_ramp[map(img_array_grey[li][i])]
            else:
                str = str + grey_ramp[map(img_array_grey[li][i])]
        str = str + '\n'
# 6: Output to terminal 
    print(str)
# 7: Save to output file
    if(save):
        with open('output.txt','w') as f:
            f.write(str)
    print(rgb(255,255,255)+"quit")

# Convert rgb values to an ANSI code 
def rgb(r,g,b):
    # Predefined ANSI color palette
    rgb = (r,g,b)
    colors = {
        (0, 0, 0): 30,     # Black
        (255, 0, 0): 31,   # Red
        (0, 255, 0): 32,   # Green
        (255, 255, 0): 33, # Yellow
        (0, 0, 255): 34,   # Blue
        (255, 0, 255): 35, # Magenta
        (0, 255, 255): 36, # Cyan
        (255, 255, 255): 37 # White
    }

    closest_color = min(colors, key=lambda c: sum(abs(x - y) for x, y in zip(c, rgb)))
    return f"\033[{colors[closest_color]}m"




if __name__ == "__main__":
    convert_grey(Image.open('fruit.jpeg'),True,2,True)

# print(rgb(255,255,255)+"quit")


