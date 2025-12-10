class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.abbrs = {}
        for word in dictionary:
            abbr = self.getAbbr(word)
            if abbr not in self.abbrs:
                self.abbrs[abbr] = set([word])
            else:
                self.abbrs[abbr].add(word)
        print(self.abbrs)

    def getAbbr(self, word):
        return (
            f"{word[0]}{len(word) - 2}{word[-1]}"
            if len(word) > 2
            else f"{word[0]}{word[-1]}"
        )

    def isUnique(self, word: str) -> bool:
        abbr = self.getAbbr(word)
        if abbr not in self.abbrs:
            return True
        elif (
            abbr in self.abbrs
            and word in self.abbrs[abbr]
            and len(self.abbrs[abbr]) == 1
        ):
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
