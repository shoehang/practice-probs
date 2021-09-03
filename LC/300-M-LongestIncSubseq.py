class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_arr = []
        for number in nums:
            if not longest_arr or longest_arr[-1] < number:
                longest_arr.append(number)
            else:
                replace_index = self.binarySearch(longest_arr, number)
                longest_arr[replace_index] = number
        return len(longest_arr)
            
    def binarySearch(self, arr, val):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return left