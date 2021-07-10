# Given a string, write a function to check if it is a permutation of a palindrome.
# Assume ignore casing and non-letter characters.
# Input: 'Tact Coa'
# Output: True --> ('taco cat', 'atco cta')

# Time Complexity: O(N + M)
# Space Complexity: O(N)
# where N is length of text M is size of hashtable

def PalindromePerm(string):
	hashTable = dict()
	# assume no characters so far
	oddChars = False
	# store in hash table O(n)
	for char in string:
		caseInsensitive = char.lower()
		if caseInsensitive != ' ':
			hashTable[caseInsensitive] = hashTable.get(caseInsensitive, 0) + 1
	# rather than try and compute all permuations that are also palindromes,
	# patterns can reduce unecessary computation
	# each char must have matching pair,
	# or ^ plus single char with odd occurences O(m)
	for occurences in hashTable.values():
		# odd occurences -> set odd found
		if occurences % 2 == 1:
			# second odd occurence found
			if oddChars:
				return False
			# otherwise set first encounter
			oddChars = True
	# return true since all else is even
	return True

print(PalindromePerm('Taco Cat'))
print(PalindromePerm('taco cat'))
print(PalindromePerm('AABBC'))
print(PalindromePerm('AABC'))
