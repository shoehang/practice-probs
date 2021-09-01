class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def dfs(index, current_string):
            if index == len(s):
                permutations.append(''.join(current_string))
                return
            if s[index].isalpha():
                current_string.append(s[index].lower())
                dfs(index+1, current_string)
                current_string.pop()
            current_string.append(s[index].upper())
            dfs(index+1, current_string)
            current_string.pop()
            
        permutations = []
        dfs(0, [])
        return permutations