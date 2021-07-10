
def combinationSum(candidates, target):
	outputArr = []
	helper(target, candidates, [], outputArr)
	return outputArr

def helper(target, candidates, combinedSum, paths):
	if target < 0:
		return 
	elif target == 0:
		paths.append(combinedSum)
		return
	else:
		for i in range(len(candidates)):
			helper(target-candidates[i], candidates[i:], combinedSum + [candidates[i]], paths)

print(combinationSum([2,3,5], 8))