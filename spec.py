#  -*- coding: utf-8 -*-

import PyPDF2, os, pyperclip
key = ['Watts', 'watts', 'Zurn' ]
# input PDF name to program

pdf = input('What is the pdf name?')

directory = 'C:\\ProjectTxtFiles\\'
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir('C:\\Users\\Patrick\\Downloads')

pdfFile = open(pdf + ".pdf", 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

newTxt = open(directory + pdf + '.txt', 'w')

for pageNum in range(reader.numPages):
    txtWall = reader.getPage(pageNum).extractText().encode("utf-8")
    newTxt.write(str(txtWall))
 
newTxt.close() 

foundTxt = open(directory + 'FOUND' + pdf + '.txt', 'w')

for i in range(len(key)):
    searchFile = open(directory + pdf + '.txt', 'r')
    for line in searchFile:
        if key[i] in line:
            foundTxt.write(key[i] + ' found\n')
        else:
            foundTxt.write(key[i] + ' not found\n')
    searchFile.close()
    
foundTxt.close()
# search over the txt file for key words 

# create a found txt file 

# send found info to the found txt file






