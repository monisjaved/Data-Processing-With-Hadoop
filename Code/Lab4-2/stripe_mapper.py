#!/usr/bin/env python

import sys
import json

for line in sys.stdin:

    line = line.strip()

    words = line.split()
    counts = {}

    for i in xrange(len(words)-1):
        counts = {}
        for j in range(i+1,len(words)):
            if words[j] not in counts:
                counts[words[j]] = 0
            counts[words[j]] += 1
        print "%s\t%s" % (words[i],json.dumps(counts))
