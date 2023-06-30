# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import argparse
import os
import re
import sys
import gzip
from unicodedata import normalize

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

parser = argparse.ArgumentParser(description='Looks up a word')
parser.add_argument('word', type=str, help='word to look up')
parser.add_argument('file', type=str, help='file of the dictionary')

 
args = parser.parse_args()
 
heading_template='<p><b><a href="bword:%s">%s</a></b></p>'


def do_search(w, file_name):
   w = normalize('NFKC', w)
   out = ""
   hits = 0

   fileobj = open(file_name,'r', encoding='utf-16le').readlines()

   for line in fileobj:
      if not line:
         continue

      if line[0] != '\t':
         # print(w, line)
         if w in line.lower():
            heading = line.rstrip()
            line = re.sub("(?<!\\\)\[[^]]+?\]", "", line)
            out += heading_template % (heading, heading)
            hits += 1

   return out

if not args.word.startswith("|"):
   print(do_search(args.word,args.file))