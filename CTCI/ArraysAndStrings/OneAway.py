# There are three types of edits that can be performed on strings: insert, remove, replace
# Given 2 strings, write a function to check if they are one edit (or zero) away.
# Example: 
# Input: 'pale', 'ple' -> true
# Output: True

# Time Complexity: O(N)
# Space Complexity: O(1)

def OneAway(string1, string2):
	# anything more than 1 means more than 1 edit
	if abs(len(string1) - len(string2)) > 1:
		return False
	# pointers to traverse string, and flag for first edit
	p1, p2 = 0, 0
	firstEdit = False
	while p1 < len(string1) and p2 < len(string2):
		# same char, move onto next
		if string1[p1] == string2[p2]:
			p1 += 1
			p2 += 1
		elif not firstEdit:
			firstEdit = True
			# replacement
			if len(string1) == len(string2):
				p1 += 1
				p2 += 1
			# insert/delete for second string
			elif len(string1) < len(string2):
				p2 += 1
			# insert/delete for first string
			elif len(string2) < len(string1):
				p1 += 1
		else:
			return False
	return True

print(OneAway('pale', 'ale'))
print(OneAway('12345', '123'))
print(OneAway('12345', '1245'))