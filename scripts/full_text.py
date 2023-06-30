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
   w = w[1:]
   out = ""
   hits = 0

   fileobj = open(file_name,'r', encoding='utf-16le').readlines()

   for line in fileobj:
      if not line:
         continue

      if line[0] != '\t':
         heading = line
         continue
      
      if not w in line:
         continue

      heading = heading.rstrip()
      line = re.sub("(?<!\\\)\[[^]]+?\]", "", line)
      p = line.find(w)
      out += heading_template % (heading, heading)
      text = "...%s..." % line[max(0, p - 40):p + 40].strip()
      for ch in "[]~":
         text = text.replace("\\" + ch, ch)
      for s in ("<<",">>"):
         text = text.replace(s,"")
      out += "<p>%s</p>" % text
      hits += 1

   if hits == 0:
      return "Nothing found"

   return out
 
if not args.word.startswith("|"): 
    print("Input a word beginning with '|' to perform a full text search.")  
else:
   print(do_search(args.word,args.file))