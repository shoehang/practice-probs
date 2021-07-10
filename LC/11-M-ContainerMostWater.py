
def maxArea(height):
	greatestArea = 0

	right = len(height) - 1 
	left = 0

	while left < right:
		leftVal = height[left]
		rightVal = height[right]
		currArea = (right - left) * min(leftVal, rightVal)
		if currArea > greatestArea:
			greatestArea = currArea
		if leftVal < rightVal:
			left += 1
		else: 
			right -= 1

	return greatestArea

penis = [4,3,4,5,6,2,1,2,3,4]

print(maxArea(penis))