import collections
from collections import Counter
import sys
import numpy as np

def swapchars(text):
	lower_text = text.lower()
	c = Counter(text)
	max = -1;
	min = sys.maxint;
	for key in c:
		if key.isalpha():
			if c[key] > max:
				max_key = key
				max = c[key]
			if c[key] < max:
				min_key = key
				min = c[key]
	if max == -1:
		print "Error: No alphabetical characters!"
		return
	else:
		new_str = text.replace(max_key, min_key)
		new_str = new_str.replace(max_key.upper(), min_key.upper())
		print new_str
	return

text = 'I\'m just a Chi-town coder with a nice flow.'
swapchars(text)

def sortcat(num, *args):
	if num > len(args) or num < 0:
		print "Error: Invalid number provided."
		return
	strs = []
	for i in args:
		strs.append(i)
	strs.sort(key=len, reverse=True)

	new_str = ''
	for i in range(num):
		new_str += strs[i]
	print new_str
	return

sortcat(1, 'abc', 'bc')
sortcat(2, 'bc', 'c', 'abc')

def bluesclues(abrv):
	text = np.loadtxt('states.txt', dtype = 'string', delimiter=',')
	for row in text:
		if row[1] == abrv:
			return row[0]
	print "Error: Abbreviation not found!"
	return

print bluesclues('AL');

def bluesbooze(state):
	text = np.loadtxt('states.txt', dtype = 'string', delimiter=',')
	for row in text:
		if row[0] == state:
			return row[1]
	print "Error: State not found!"
	return

print bluesbooze('Alabama');

