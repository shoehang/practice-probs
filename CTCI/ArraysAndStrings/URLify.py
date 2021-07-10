# Write a method to replace all spaces in a string with '%20'.
# Assume input contains true length (including spaces).
# Example: 
# Input: 'Mr John Smith', 13
# Output: 'Mr%20John%20Smith'

# Time Complexity: O(N)
# Space Complexity: O(N - S + 3S)
# where N is length of text and S is number of whitespace

def URLify(text, textlength):
	spaces = 0
	# find spaces. O(N) operation
	for char in text:
		if char == ' ':
			spaces += 1
	# create array for url
	url = [None] * (textlength - spaces + (spaces * 3))
	unextended = len(text) - 1
	extended = len(url) - 1
	# using pointers for traversal starting tail
	# string indexing is O(1)
	while unextended >= 0 and extended >= 0:
		if text[unextended] == ' ':
			url[extended] = '0'
			url[extended - 1] = '2'
			url[extended - 2] = '%'
			unextended -= 1
			extended -= 3
		else:
			url[extended] = text[unextended]
			unextended -= 1
			extended -= 1
	return url

print(URLify('Mr John Smith', 13))
print(URLify('Mr John Smith Doe', 17))