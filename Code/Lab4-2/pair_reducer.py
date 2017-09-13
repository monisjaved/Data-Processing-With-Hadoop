#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:

    line = line.strip()

    wordpair, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == wordpair:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = wordpair

if current_word == wordpair:
    print '%s\t%s' % (current_word, current_count)
