#!/usr/bin/env python

from operator import itemgetter
import sys
import json

current_word = None
current_dict = {}
word = None


for line in sys.stdin:

    line = line.strip()


    word, stripe = line.split('\t', 1)


    try:
        stripe = json.loads(stripe)
    except:
        print "error"
        continue

    if current_word == word:
        for entries in stripe:
            if entries not in current_dict:
                current_dict[entries] = 0
            current_dict[entries] += int(stripe[entries])
    else:
        if current_word:

            print '%s\t%s' % (current_word, json.dumps(current_dict))
        current_dict = stripe
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word, json.dumps(current_dict))
