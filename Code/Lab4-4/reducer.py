#!/usr/bin/env python

from operator import itemgetter
from itertools import product
import sys
import csv

current_word = None
current_set = set()
current_lemmas = []
word = None


lemma = {}
f = open("la.lexicon.csv", "rb")
reader = csv.reader(f)
for row in reader:
    row = [i.lower() for i in row if i != ""]
    if row[0] not in lemma:
        lemma[row[0]] = []
    if row[2] not in lemma[row[0]]:
        lemma[row[0]].append(row[2])


for line in sys.stdin:

    line = line.strip()

    wordpair, loc = line.split('\t', 1)

    if current_word == wordpair:
        current_set.add(loc)
    else:
        if current_word:
            tuples = list(product(*current_lemmas))
            for tup in tuples:
                word = "{" + ", ".join(tup) + "}"
                print "%s\t%s" % (word,", ".join(current_set))

        current_word = wordpair
        current_set = set()
        current_set.add(loc)

        wordpair = [i.strip() for i in wordpair.split(", ")]
        current_lemmas = []
        for word in wordpair:
            if word in lemma:
                current_lemmas.append(lemma[word])
            else:
                current_lemmas.append([word])

if current_word == wordpair:
    tuples = list(product(*current_lemmas))
    for tup in tuples:
        word = "{" + ", ".join(tup) + "}"
        print "%s\t%s" % (word,", ".join(current_set))