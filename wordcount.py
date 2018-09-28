# put your code here.
import sys 

import_file = open(sys.argv[1], "r")

def word_counts(file_1):
	words = {}
	for line in file_1:
		line = line.strip().split()
		for word in line:
			if word in words:
				words[word] = word.get(words, 0) + 1  
	return words

dictionary_of_word_counts = word_counts(import_file)
print(dictionary_of_word_counts)