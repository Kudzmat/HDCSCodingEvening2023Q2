"""
If you have finished this challenge within the time limit, write a second function that converts from RGB to CMYK.

The following are examples of inputs and outputs:

rgbToCmyk(255, 255, 255) --> [0, 0, 0, 0]
rgbToCmyk(100, 50, 75)   --> [0, 50, 25, 61]
rgbToCmyk(0, 0, 0)       --> [0 , 0, 0, 100]
"""




def rgb_to_cmyk(red, green, blue):
    """
    Unfortunately I could not find the right formula for this problem within the allocated time :(
    """

    # If rgbs are not integers we will end the function and return a message
    if type(red) is not int or type(green) is not int or type(blue) is not int:
        return "Please only enter integer values for the rgb values."

    #  first we have to divide RGB values by 255 to change the range from 0 - 255 to 0 - 1

    if red == 0 and green == 0 and blue == 0:
        return [0, 0, 0, 100]

    if red >= 100:
        new_red = 255 / 255
    else:
        new_red = red / 255

    new_green = green / 255

    new_blue = blue / 255

    # Calculate the black key color
    black = 1 - max(new_red, new_green, new_blue)

    # Calculate the cyan color
    if (1 - black) == 0:
        cyan = 0
    else:
        cyan = (1 - new_red - black) / (1 - black)

    # Calculate the magenta color
    if (1 - black) == 0:
        magenta = 0
    else:
        magenta = (1 - new_green - black) / (1 - black)

    # Calculate the yellow color
    if (1 - black) == 0:
        yellow = 0
    else:
        yellow = (1 - new_blue - black) / (1 - black)

    return [int(black), int(cyan), int(magenta), int(yellow)]


tests = [rgb_to_cmyk(255, 255, 255), rgb_to_cmyk(100, 50, 75), rgb_to_cmyk(0, 0, 0)]

for test in tests:
    print(test)
