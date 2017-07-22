#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
# KEYWORDS MUST BE LOWERCASE

import PyPDF2
import os
import re
import sys
from dictionary import Dictionary

pdf = input('What is the pdf name?')

# directory = 'C:\\Projects\\SpecCrawl\\' # Windows
# dictionary = "C:\\Projects\\SpecCrawl\\keywords" # Windows
# file = "C:\\Projects\\SpecCrawl\\testtxt" # Windows

# path = 'C:\\Users\\pbodin\\Downloads' # work PC
# path = 'C:\\Users\\Patrick\\Downloads' # home PC

directory = '/home/patrick/Projects/SpecCrawl/' # Linux
dictionary = '/home/patrick/Projects/SpecCrawl/keywords' # Linux
file = "/home/patrick/Projects/SpecCrawl/testtxt"
path = '/home/patrick/Downloads/' # Linux

foundSet = set()
LENGTH = 20

if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(path)

pdfFile = open(pdf + ".pdf", 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
newTxt = open(directory + 'testtxt', 'w')

for pageNum in range(reader.numPages):
    txtWall = reader.getPage(pageNum).extractText().encode("utf-8")
    newTxt.write(str(txtWall))
newTxt.close()

d = Dictionary()
loaded = d.load(dictionary)

if not loaded: 
    print("Could not load $dictionary.")
    exit(1)

fp = open(file, "r", encoding="utf-8")
if not fp:
    print("Could not open {}.".format(file))
    exit(2)

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
                foundSet.add(word)
                print(word)
                findings += 1
    elif re.match(r'[\s]', c):
            words += 1
            index, word = 0, ""
fp.close()

n = d.size()
unloaded = d.unload()

if not unloaded:
    print("Could not unload dictionary.")
    exit(3)

print("\nWORDS FOUND:     {}".format(findings))
print("WORDS IN DICTIONARY:  {}".format(n))
print("WORDS IN TEXT:        {}".format(words))
print(foundSet)

# KEYWORDS MUST BE LOWERCASE