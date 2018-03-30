import webbrowser
import argparse
import pyperclip
parser = argparse.ArgumentParser(description='open google maps location')
parser.add_argument('-l', '--location',type=str, help='enter the location address')
args = parser.parse_args()

clipped_word = ''
if args.location:
    clipped_word = args.location
else:
    clipped_word = pyperclip.paste()




webbrowser.open('http://maps.google.com/maps/place/{0}'.format(clipped_word))