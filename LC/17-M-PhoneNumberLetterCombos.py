class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        combinations = []
        if not digits:
            return []
        
        self.dfs(digits, 0, dic, '', combinations)
        return combinations

    def dfs(self, digits, index, dic, combinationstring, combinations):
        if index >= len(digits):
            combinations.append(combinationstring)
            return
        tempstring = dic[digits[index]]
        
        for char in tempstring:
            self.dfs(digits, index + 1, dic, combinationstring + char, combinations)