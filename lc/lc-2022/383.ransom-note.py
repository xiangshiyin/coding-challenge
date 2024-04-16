#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        target = Counter(ransomNote)
        source = Counter(magazine)
        for l,f in target.items():
            if l not in source:
                return False
            else:
                if f > source[l]:
                    return False
        return True
        
# @lc code=end

