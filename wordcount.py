# put your code here.
import sys, re

import_file = open(sys.argv[1], "r")

def word_counts(file_1):
	words = {}
	for line in file_1:
		line = line.strip().lower()
		line = re.sub(r'[^a-z ]', '', line).split()
		for word in line:
			words[word] = words.get(word, 0) + 1
	return words

dictionary_of_word_counts = word_counts(import_file)
print(dictionary_of_word_counts)