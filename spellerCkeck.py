# #!/usr/bin/env python3

# import re
# import sys
# from dictionary import Dictionary

# LENGTH = 15

# dictionary = "C:\\Projects\\SpecCrawl\\keywords"

# d = Dictionary()
# loaded = d.load(dictionary)

# if not loaded: 
#     print("Could not load $dictionary.")
#     exit(1)

# file = "C:\\Projects\\SpecCrawl\\testtxt"
# fp = open(file, "r", encoding="utf-8")
# if not fp:
#     print("Could not open {}.".format(file))
#     exit(1)

# print("\nFOUND WORDS\n")
# word = ""
# index, findings, words = 0, 0, 0

# while True:
#     c = fp.read(1)
#     if not c:
#         break
#     if re.match(r'[\S]', c):
#         word += c
#         index += 1
#         if index > LENGTH:
#             while True:
#                 c = fp.read(1)
#                 if not c or not re.match(r'[\S]', c):
#                     break
#             index, word = 0, ""
#         elif index > 0:
#             found = d.check(word)
#             if found:
#                 print(word)
#                 findings += 1
#     elif re.match(r'[\s]', c):
#             words += 1
#             index, word = 0, ""
# fp.close()

# n = d.size()
# unloaded = d.unload()

# if not unloaded:
#     print("Could not load $dictionary.")
#     exit(1)

# print("\nWORDS FOUND:     {}".format(findings))
# print("WORDS IN DICTIONARY:  {}".format(n))
# print("WORDS IN TEXT:        {}".format(words))