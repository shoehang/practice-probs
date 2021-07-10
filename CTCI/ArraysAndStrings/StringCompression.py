# Write a method to perform basic string compression using the counts of repeated characters.
# If the compressed string is not smaller than the original, return the original
# Example:
# Input: 'aaabbcccaaaaa'
# Output: 'a3b2c3a5'

# Time Complexity: O(N)
# Space Complexity: O(N)

def StringCompression(string):
	compressedString = []
	# curr char
	c = string[0]
	# curr repeated char
	counter = 1
	for char in string[1:]:
		if c == char:
			counter += 1
		else:
			compressedString.append(c)
			compressedString.append(str(counter))
			c = char
			counter = 1
	# add whatevers left over
	compressedString.append(c)
	compressedString.append(str(counter))
	compressedString = "".join(compressedString)
	# length check
	if len(string) < len(compressedString):
		return string
	return compressedString

print(StringCompression('abcd'))
print(StringCompression('aaabbbcccddd'))
print(StringCompression('aabbccdd'))