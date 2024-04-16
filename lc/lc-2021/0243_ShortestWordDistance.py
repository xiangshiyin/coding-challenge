'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # step 0: empty words list
        if (len(words)==0)|(word1==None)|(word2==None):
            return None
        # step 1: create pools of index
        idx1 = -1
        idx2 = -1
        dist = -1
        
        # step 2: traverse the list of words
        for idx,w in enumerate(words):
            if w==word1:
                idx1 = idx
            elif w==word2:
                idx2 = idx
            if (idx1>=0)&(idx2>=0):
                if dist == -1:
                    dist = abs(idx1-idx2)
                elif abs(idx1-idx2)<dist:
                    dist = abs(idx1-idx2)
            # print(idx, w, idx1, idx2, dist==-1)
        if dist==-1:
            return None
        else:
            return dist
        

