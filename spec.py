#  -*- coding: utf-8 -*-

import PyPDF2, os, pyperclip
key = ['sloan' ]
# input PDF name to program

pdf = input('What is the pdf name?')

directory = 'C:\\ProjectTxtFiles\\'
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir('C:\\Users\\pbodin\\Downloads')

pdfFile = open(pdf + ".pdf", 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

newTxt = open(directory + pdf + '.txt', 'a')
foundTxt = open(directory + 'FOUND' + pdf + '.txt', 'a')

for pageNum in range(reader.numPages):
    txtWall = reader.getPage(pageNum).extractText().encode("utf-8")
    newTxt.write(str(txtWall))
    for i in range(len(key)-1):
        if key[i] in txtWall.lower():
            foundTxt.write(key[i] + 'found in page ' + pageNum + "/n")
 
newTxt.close()            
foundTxt.close()
# search over the txt file for key words 

# create a found txt file 

# send found info to the found txt file






