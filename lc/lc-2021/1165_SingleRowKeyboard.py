class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # create hash table to record the index of characters
        tb = {char: i for i, char in enumerate(keyboard)}
        # print(tb)
        time = 0

        for j in range(len(word)):
            if j == 0:
                time += tb[word[j]]
                # print(time)
            else:
                time += abs(tb[word[j]] - tb[word[j - 1]])
                # print(time)

        return time
