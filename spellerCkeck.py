#!/usr/bin/env python3

import re
import sys
import time
from dictionary import Dictionary

LENGTH = 11

WORDS = "C:\\Projects\\SpecCrawl\\keywords"

dictionary = sys.argv[1] if len(sys.argv) == 3 else WORDS

d = Dictionary()
loaded = d.load(dictionary)

if not loaded: 
    print("Could not load $dictionary.")
    exit(1)

file = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]
fp = open(file, "r", encoding="latin_1")
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
    if re.match(r"[A-Za-z]", c) or (c == "-") or re.match(r"[0-9]", c):
        word += c
        index += 1
        if index > LENGTH:
            while True:
                c = fp.read(1)
                if not c or not re.match(r"[A-Za-z]", c) or (c == "-") or re.match(r"[0-9]", c):
                    break
            index, word = 0, ""
    elif index > 0:
        words += 1
        found = d.check(word)
        if found:
            print(word)
            findings += 1
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