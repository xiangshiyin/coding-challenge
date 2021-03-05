class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = ['']
        for char in S:
            if char.isalpha():
                result = [r + ch for r in result for ch in [char.lower(), char.upper()]]
            else:
                result = [r + char for r in result]
        return result
    