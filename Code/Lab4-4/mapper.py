#!/usr/bin/env python

import sys
from itertools import combinations,product
import re
from string import punctuation
import csv

punct = list(punctuation)
n = int(sys.argv[1])

for line in sys.stdin:

    line = line.strip().lower()

    line = re.sub("\s+"," ",line)

    if(len(line.split("> ")) != 2):
        continue

    loc, words = line.split("> ")
    loc += ">"

    words = "".join([i for i in words.replace("j","i").replace("v","u") if i not in punct])
    words = words.strip().split()

    for i in xrange(len(words)):
        words[i] = [words[i]]


    for x in combinations(range(len(words)),n):
        flag = True
        for i in range(len(x)-1):
                if x[i] >= x[i+1]:
                        flag = False
                        break
        if flag is True:
            tuples = list(product(*[words[i] for i in x]))
            for tup in tuples:
                word = ", ".join(tup)
                print "%s\t%s" % (word,loc)