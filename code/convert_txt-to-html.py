#Python 2.7
#Christopher Church
#Doten Diaries

from os import listdir
import csv

current_newspaper = "territorial"

mypath="../assets/"+current_newspaper+"/txt"
files = [f for f in listdir(mypath) if f.endswith(".txt")]

def getText(filename):
    with open(filename,"rb") as infile:
        lines = infile.readlines()
    html=""
    for line in lines:
        html = html + "<p>"+line+"</p>"
    return html.replace("\n","")
    
outfile_csv = open(current_newspaper+".csv","wb")
w = csv.writer(outfile_csv)
w.writerow(["news_id","html","image_uri","publication"])
print files

for file in files:
    text = getText(mypath+"/"+file)
    w.writerow([file.split(".")[0],text,"public://"+current_newspaper+"/"+file.split(".")[0]+".jpg",current_newspaper])
outfile_csv.close()

print "Success!"