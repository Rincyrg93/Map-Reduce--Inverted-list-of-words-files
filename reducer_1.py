#!/usr/bin/env python 
import sys
import os
import re

if __name__== "__main__":
	current_word=None
	
	file_names=[]
	for line in sys.stdin:
		
		w,fn= line.split("\t")
		fn=fn.strip()
		
		if w == current_word:
			
			
			if fn not in file_names:
				file_names.append(fn)	
		else:
			if current_word is not None:
				sys.stdout.write("{0}\t{1}\n".format(current_word,file_names))
					
			current_word=w
			file_names=[]
			file_names.append(fn)			
	if current_word:
		sys.stdout.write("{0}\t{1}\n".format(current_word,file_names))

			
