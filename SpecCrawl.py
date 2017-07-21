#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import PyPDF2
import os
import re
import sys
from dictionary import Dictionary

pdf = input('What is the pdf name?')

directory = 'C:\\Projects\\SpecCrawl\\'
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir('C:\\Users\\pbodin\\Downloads')    # work computer
# os.chdir('C:\\Users\\Patrick\\Downloads')    # home computer

pdfFile = open(pdf + ".pdf", 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

newTxt = open(directory + 'testtxt', 'w')

for pageNum in range(reader.numPages):
    txtWall = reader.getPage(pageNum).extractText().encode("utf-8")
    newTxt.write(str(txtWall))
 
newTxt.close()

LENGTH = 15

dictionary = "C:\\Projects\\SpecCrawl\\keywords"

d = Dictionary()
loaded = d.load(dictionary)

if not loaded: 
    print("Could not load $dictionary.")
    exit(1)

file = "C:\\Projects\\SpecCrawl\\testtxt"
fp = open(file, "r", encoding="utf-8")
if not fp:
    print("Could not open {}.".format(file))
    exit(1)

print("\nFOUND WORDS\n")
word = ""
index, findings, words = 0, 0, 0

while True:
    c = fp.read(1)
    if not c:
        break
    if re.match(r'[\S]', c):
        word += c
        index += 1
        if index > LENGTH:
            while True:
                c = fp.read(1)
                if not c or not re.match(r'[\S]', c):
                    break
            index, word = 0, ""
        elif index > 0:
            found = d.check(word)
            if found:
                print(word)
                findings += 1
    elif re.match(r'[\s]', c):
            words += 1
            index, word = 0, ""
fp.close()

n = d.size()
unloaded = d.unload()

if not unloaded:
    print("Could not load $dictionary.")
    exit(1)

print("\nWORDS FOUND:     {}".format(findings))
print("WORDS IN DICTIONARY:  {}".format(n))
print("WORDS IN TEXT:        {}".format(words))