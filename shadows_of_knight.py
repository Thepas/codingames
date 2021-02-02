import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [10, 10]
n = 10  # maximum number of turns before game over.
x0, y0 = [2, 5]  # position batman
w0, h0 = 0, 0

# game loop
while True:
    bomb_dir = "U"  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # si la bombe est en haut
    if "U" in bomb_dir:
        h = y0  # on réduit la hauteur
        y0 = math.floor((y0 + h0)/2)
    # Si la bombe est en bas
    if "D" in bomb_dir:
        h0 = y0
        y0 = math.floor((y0 + h)/2)

    if "R" in bomb_dir:
        w0 = x0
        x0 = math.floor((x0 + w)/2)

    if "L" in bomb_dir:
        w = x0
        x0 = math.floor((x0 + w0)/2)

    # the location of the next window Batman should jump to.
    print(str(int(x0)) + " " + str(int(y0)))
