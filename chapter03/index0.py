#coding:utf-8

import sys
import re

WORD_RE = re.compile(r'\w+')

#sys.argv[1] = './data/zen.txt'

index = {}
with open('./data/zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])