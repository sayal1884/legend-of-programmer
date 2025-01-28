from PIL import Image
from tkinter import *
import PIL
import glob, os
def tef():
    global prin
    for infile in glob.glob("*.png"):
        file, ext = os.path.splitext(infile)
        try:
            prin.append("games/item/"+infile)
        except:
            pass
    print(prin)
fen=Tk()
prin=[]
widthH=fen.winfo_screenwidth()
heightH=fen.winfo_screenheight()
tef()
