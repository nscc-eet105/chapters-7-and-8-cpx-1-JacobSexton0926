import board
import neopixel
import random
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3, auto_write=False)

with open("/pattern.txt", "r") as file:
    line = file.readline()
    pattern = [int(x) for x in line.split(", ")]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


while True:
    for i in pattern:
        color = random_color()

        pixels[i] = color
        pixels.show()

        time.sleep(0.2)

        pixels[i] = (0, 0, 0)
        pixels.show()

        time.sleep(0.1)# Write your code here :-)
