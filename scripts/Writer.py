from PIL import Image
from fpdf import FPDF
import sys
import argparse
import cv2
import os
import time

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--font", required=True, help="font")
args = vars(ap.parse_args())

os.makedirs("../Output", exist_ok=True)
os.makedirs("../PDF_Outputs", exist_ok=True)

background = Image.open("../Fonts/myfont/a4.jpg")
SheetWidth = background.width
margin = 115
lineMargin = 115
allowedCharacters = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ 
                        abcdefghijklmnopqrstuvwxyz 
                        #:,.?-!{}()[]'<>+=%^$@_;1234567890 "'''

wordsPerLine = 80
maxLenPerPage = 3349
pageNum = 1

filePath = "../input.txt"
writing = args["font"]