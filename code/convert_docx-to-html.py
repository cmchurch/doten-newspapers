import mammoth
from os import listdir
import csv

mypath="."
files = [f for f in listdir(mypath) if f.endswith(".docx")]

def getText(filename):
    with open(filename,"rb") as infile:
	    html = mammoth.convert_to_html(infile)
    return html.value
	
outfile_csv = open("Rock_html.csv","w")
w = csv.writer(outfile_csv)

for file in files:
	text = getText(file)
	f = open(file[:-4]+"html","w") 
	f.write(text) 
	f.close()
	w.writerow([file[:-5],text,"public://rock/"+file[:-5]+".jpg"])
outfile_csv.close()