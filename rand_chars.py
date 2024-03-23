"""
FILE:		rand_chars.py
TITLE:		Return and Generate Strings of Random Characters
AUTHOR:		Daniel R. South
"""

import random
from random import randint

char_list = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_index = len(char_list) - 1

#
# Function to return a string of random characters
def get_rand_str(num_chars):
	rand_str = ""
	for n in range(0,num_chars):
		j = randint(0, max_index)
		rand_str = rand_str + char_list[j]

	return rand_str


#
# Generator to generate an iterable of random characters
def gen_rand_chars(max_chars):
	n = 0
	while n < max_chars:
		j = randint(0, max_index)
		yield(char_list[j])
		n = n + 1


print("\nLet's make some strings of random characters!\n")

str1 = get_rand_str(4)
print(str1 + "\t" + str(len(str1)) + " characters")

str2 = get_rand_str(12)
print(str2 + "\t" + str(len(str2)) + " characters")

str3 = get_rand_str(37)
print(str3 + "\t" + str(len(str3)) + " characters")


print("\nNow, let's generate an iterable with 23 random characters!")

for c in gen_rand_chars(23):
	print(c)

