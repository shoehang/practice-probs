# Implement an algorithm to determine if a string has all unique characters.
# What if you cannont use any additional data structures?

from BasicHashTable import *

# Time Complexity: O(N)
# Space Complexity: O(N)
# where N is length of string

def IsUnique(string):
	hashTable = HashTable()
	for character in string:
		# looks for if char already inserted. *O(1) operation
		if hashTable.find(character) == character:
			return False
		else:
			# insert if char is new. *O(1) operation
			hashTable.insert(character, character)
	return True

print(IsUnique("abcdefghijk"))
print(IsUnique("abcdefghijkk"))