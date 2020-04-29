#! python 3
# mapIt.py -Launches a map in the browser using address from
# the command line or clipboard

import sys
import webbrowser
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
