import PyPDF2, os, pyperclip

# input PDF to program

# create a new txt file for the pdf

# save the output of the pdf to the txt file

# search over the txt file for key words 

# create a found txt file 

# send found info to the found txt file


os.chdir('C:\\Users\\pbodin\\Downloads')

pdfFile = open('Annapolis Yacht Club FTP PLMB SPECS.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

page = reader.getPage(0)

text = page.extractText()

for pageNum in range(reader.numPages):




