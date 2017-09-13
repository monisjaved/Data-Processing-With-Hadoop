#!/usr/bin/env python

from operator import itemgetter
import sys

import csv

lemma = {}
f = open("la.lexicon.csv", "rb")
reader = csv.reader(f)
for row in reader:
    row = [i.lower() for i in row if i != ""]
    if row[0] not in lemma:
        lemma[row[0]] = []
    if row[2] not in lemma[row[0]]:
        lemma[row[0]].append(row[2])

current_word = None
current_lemmas = []
current_locs = []
word = None


for line in sys.stdin:

    line = line.strip()

    if len(line.split("\t")) != 2:
        continue


    word, loc = line.split('\t')


    word = word.strip()

    if current_word == word:
        current_locs.append(loc)
    else:
        if current_word:
            if len(current_lemmas) == 0:
                print '%s\t%s' % (current_word,", ".join(current_locs))

            else:
                for lemm in current_lemmas:
                    print '%s\t%s' % (lemm,", ".join(current_locs))

        if word in lemma:
            current_lemmas = lemma[word]
        else:
            current_lemmas = []
        
        current_word = word
        current_locs = [loc]

if current_word == word:
    if current_word:
        if len(current_lemmas) == 0:
            print '%s\t%s' % (current_word,", ".join(current_locs))

        else:
            for lemm in current_lemmas:
                print '%s\t%s' % (lemm,", ".join(current_locs))