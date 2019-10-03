from os import listdir
from PIL import Image

mypath="."
files = [f for f in listdir(mypath) if f.endswith(".tif")]

def parse_tif(filePath):
    img = Image.open(filePath)
    for i in range (numFramesPerTif):
        try:
            img.seek(i)
            img.save('file[:-4]_%s.jpg'%(i,))
        except EOFError: #end of file error

for file in files:
	parse_tif(file)