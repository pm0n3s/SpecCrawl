#!/usr/bin/env python3

import re
import sys
import time
from dictionary import Dictionary

# maximum length for a word
# (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
LENGTH = 11

# default dictionary
WORDS = "C:\\Projects\\SpecCrawl\\keywords"

# check for correct number of args
# if len(sys.argv) != 2 and len(sys.argv) != 3:
#     print("Usage: ./speller [dictionary] text")
#     exit(1) 

# benchmarks
time_load, time_check, time_size, time_unload = 0.0, 0.0, 0.0, 0.0

# determine dictionary to use
dictionary = sys.argv[1] if len(sys.argv) == 3 else WORDS

# load dictionary
d = Dictionary()
before = time.process_time()
loaded = d.load(dictionary)
after = time.process_time()

# abort if dictionary not loaded
if not loaded: 
    print("Could not load $dictionary.")
    exit(1)

# calculate time to load dictionary
time_load = after - before

# try to open file
file = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]
fp = open(file, "r", encoding="latin_1")
if not fp:
    print("Could not open {}.".format(file))
    exit(1)

# prepare to report found
print("\nFOUND WORDS\n")

# prepare to search
word = ""
index, findings, words = 0, 0, 0

# check each word in file
while True:
    c = fp.read(1)
    if not c:
        break
    
    # allow alphabetical characters and apostrophes (for possessives)
    if re.match(r"[A-Za-z]", c) or (c == "-" and index > 0):

        # append character to word
        word += c
        index += 1

        # ignore alphabetical strings too long to be words
        if index > LENGTH:

            # consume remainder of alphabetical string
            while True:
                c = fp.read(1)
                if not c or not re.match(r"[A-Za-z]", c):
                    break

            # prepare for new word
            index, word = 0, ""

    # we must have found a whole word
    elif index > 0:

        # update counter
        words += 1

        # check word's spelling
        before = time.process_time()
        found = d.check(word)
        after = time.process_time()

        # update benchmark
        time_check += after - before

        # print word if misspelled
        if found:
            print(word)
            findings += 1

        # prepare for next word
        index, word = 0, ""

# close file
fp.close()

# determine dictionary's size
before = time.process_time()
n = d.size()
after = time.process_time()

# calculate time to determine dictionary's size
time_size = after - before

# unload dictionary
before = time.process_time()
unloaded = d.unload()
after = time.process_time()

# abort if dictionary not unloaded
if not unloaded:
    print("Could not load $dictionary.")
    exit(1)

# calculate time to determine dictionary's size
time_unload = after - before

# report benchmarks

print("\nWORDS MISSPELLED:     {}".format(findings))
print("WORDS IN DICTIONARY:  {}".format(n))
print("WORDS IN TEXT:        {}".format(words))
print("TIME IN load:         {:.2f}".format(time_load))
print("TIME IN check:        {:.2f}".format(time_check))
print("TIME IN size:         {:.2f}".format(time_size))
print("TIME IN unload:       {:.2f}".format(time_unload))
print("TOTAL TIME:           {:.2f}\n".format(time_load + time_check + time_size + time_unload))

# foundTxt = open(directory + 'FOUND' + pdf + '.txt', 'w')

# for i in range(len(key)):
#     searchFile = open(directory + pdf + '.txt', 'r')
#     for line in searchFile:
#         if key[i] in line:
#             foundTxt.write(key[i] + ' found\n')
#         else:
#             foundTxt.write(key[i] + ' not found\n')
#     searchFile.close()
    
# foundTxt.close()