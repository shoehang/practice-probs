
def threeSumClosest(nums, target):
	nums.sort()

	closestSum = 99999999
	for i in range(len(nums)):
		
		smallWindow = i+1
		largeWindow = len(nums)-1
		while smallWindow < largeWindow:
			currentSum = nums[i] + nums[smallWindow] + nums[largeWindow]
			if abs(target-currentSum) < abs(target-closestSum):
				closestSum = currentSum
			if currentSum < target:
				smallWindow += 1
			else:
				largeWindow -= 1
	return closestSum
x = [-1,2,1,-4]

print(threeSumClosest(x, 1))
