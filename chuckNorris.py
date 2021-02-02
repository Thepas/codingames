import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def binToNorris(msg):
    norris = ""
    i = 0

    while i < len(msg):
        c = msg[i]
        j = 1

        while (i + j) < len(msg) and (msg[i + j] == c):
            j += 1

        if c == "0":
            norris += "00 "
        else:
            norris += "0 "

        i = i + j
        code = "0" * j
        norris += code + " "

    print(f"Debug messages...{norris}", file=sys.stderr, flush=True)

    return norris


def strToBin(msg):
    value_list = []
    result = ""

    for char in msg:
        value_list.append(bin(ord(char))[2:])

    bin_text = ''.join(value_list)

    while len(bin_text) < 7:
        bin_text = "0" + bin_text

    result += bin_text
    return result


message = "%"
bin_message = strToBin(message)
norris_message = binToNorris(bin_message)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(bin_message)
print(norris_message)
