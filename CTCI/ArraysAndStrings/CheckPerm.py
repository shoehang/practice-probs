# Given two strings, write a method to decide if one is a permutation of the other.

from BasicHashTable import *

# Time Complexity: O(N)
# Space Complexity: O(N)
# where N is length of string1.

def checkPermutation(string1, string2):
	# we know one is not perm of the other if length differs
	if len(string1) != len(string2):
		return False
	else:
		hashTable = HashTable()
		# insert each char into hash table. *O(1) operation
		for character in string1:
			hashTable.insert(character, character)
		# try to remove char from hash table. *O(1) operation
		for character in string2:
			# false if char doesnt exist
			if hashTable.remove(character) == None:
				return False
		return True

print(checkPermutation("Cat in The Hat", "Hat in The Cat"))
print(checkPermutation("ABCDEFG", "ABCDEFF"))