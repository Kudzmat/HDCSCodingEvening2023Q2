"""
NO GENERATIVE AI SUCH AS CHATGPT, BARD, BINGCHAT ETC. IS ALLOWED!
SOLUTIONS ARE MEANT TO BE YOUR OWN ATTEMPT AT THE PROBLEM AND PLAGIARISM USING CODE SNIPPETS FROM ONLINE IS NOT ALLOWED!

You will be required to also leave comments that clearly explain how your code works.

-------------------------------------------------------------------------------------------------------------------------
PROBLEM STATEMENT:

Create a function that takes the RGB values of a colour and converts it to the corresponding HEX value for that colour.

The function should take 3 arguments, the red value, the green value and the blue value.

The function should return the HEX value represented as a string. Example inputs and outputs can be found below:

rgbToHex(255, 255, 255) --> "FFFFFF"
rgbToHex(255, 255, 300) --> "FFFFFF"
rgbToHex(0, 0, 0)       --> "000000"
rgbToHex(148, 0, 211)   --> "9400D3"

The use of any prebuilt hex conversion functions/libraries WILL NOT be allowed to solve this problem.

Extra credit is awarded for code that takes edge cases into account.
Extra credit is awarded for writing unit tests. These unit tests should also test for the edge cases.

If you have finished this challenge within the time limit, write a second function that converts from RGB to CMYK.

The following are examples of inputs and outputs:

rgbToCmyk(255, 255, 255) --> [0, 0, 0, 0]
rgbToCmyk(100, 50, 75)   --> [0, 50, 25, 61]
rgbToCmyk(0, 0, 0)       --> [0 , 0, 0, 100]
"""

# This dictionary represents hexadecimal number system
# Each number from 1 - 15 is mapped to a hex equivalent
HEX_MAP = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}


def rgb_to_hex(red, green, blue):
    # we need to get the first and second values (x and y) for red, green and blue to make up the full hex
    # we do this by dividing each value by 16 (x) and then getting the remainder which will be y
    # we will then map each x and y to it's corresponding hex using our dictionary

    # If rgbs are not integers we will end the function and return a message
    if type(red) is not int or type(green) is not int or type(blue) is not int:
        return "Please only enter integer values for the rgb values."

    hex_value = ""  # Empty string will hold the final hex value

    # red values
    if red <= 0:
        hex_value += "00"  # 0 or negative values automatically set to 00

    elif red >= 250:
        hex_value += "FF"  # 250 is max so anything over 255 is automatically FF

    else:
        # get x value
        red_x = red // 16

        # map x value
        red_hex_1 = map_x(red_x)
        hex_value += red_hex_1

        # get y value
        red_y = red % 16

        # map y value
        red_hex_2 = map_y(red_y)
        hex_value += red_hex_2

    # green values
    if green <= 0:
        hex_value += "00"

    elif green >= 250:
        hex_value += "FF"

    else:

        # get x value
        green_x = green // 16

        # map x value
        green_hex_1 = map_x(green_x)
        hex_value += green_hex_1

        # get y value
        green_y = green % 16

        # map y value
        green_hex_2 = map_y(green_y)
        hex_value += green_hex_2

    # blue values
    if blue <= 0:
        hex_value += "00"

    elif blue >= 250:
        hex_value += "FF"

    else:

        # get x value
        blue_x = blue // 16

        # map x value
        blue_hex_1 = map_x(blue_x)
        hex_value += blue_hex_1

        # get y value
        blue_y = blue % 16

        # map y value
        blue_hex_2 = map_y(blue_y)
        hex_value += blue_hex_2

    return hex_value


# This function will map all the x values to a hexadecimal
def map_x(x):
    if x in HEX_MAP.keys():
        return HEX_MAP[x]


# This function will map all the y values to a hexadecimal
def map_y(y):
    if y in HEX_MAP.keys():
        return HEX_MAP[y]


tests = [rgb_to_hex(255, 255, 255),
         rgb_to_hex(255, 255, 300),
         rgb_to_hex(0, 0, 0),
         rgb_to_hex(148, 0, 211),
         rgb_to_hex(148.23, 0, 211),
         rgb_to_hex(220, 20, 60),
         rgb_to_hex(150, "hi", 211),
         rgb_to_hex(-150, -4, -211)
         ]

for test in tests:
    print(test)
