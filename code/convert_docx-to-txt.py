import docx
from os import listdir
import csv

mypath="."
files = [f for f in listdir(mypath) if f.endswith(".docx")]

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
	
outfile_csv = open("Rock.csv","w")
w = csv.writer(outfile_csv)
for file in files:
	text = getText(file)
	f = open(file[:-4]+"txt","w") 
	f.write(text) 
	f.close()
	w.writerow([file[:-4],text])
outfile_csv.close()