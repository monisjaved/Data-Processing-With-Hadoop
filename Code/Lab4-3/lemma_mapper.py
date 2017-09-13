#!/usr/bin/env python

import sys
from string import punctuation
import re

punct = list(punctuation)

for line in sys.stdin:

    line = line.strip()

    line = re.sub("\s+", " ", line)

    if len(line.split("> ")) != 2:
        continue

    loc,words = line.split("> ")
    loc += ">"

    words = words.strip().split()
    for word in words:
        word = word.strip()
        
        word = "".join([i for i in word if i not in punct])

        word = word.replace("j","i")
        word = word.replace("J","I")
        word = word.replace("v","u")
        word = word.replace("V","U")
        word = word.lower()
        
        print '%s\t%s' % (word,loc)
