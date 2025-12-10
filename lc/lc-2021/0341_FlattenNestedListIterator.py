# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # flattern the input list
        self.flattened = self.flatten(nestedList)[::-1]

    def flatten(self, nestedList):
        res = []

        for nl in nestedList:
            if nl.isInteger():
                res.append(nl.getInteger())
            else:
                res += self.flatten(nl.getList())
        return res

    def next(self) -> int:
        if self.hasNext():
            return self.flattened.pop()
        else:
            return None

    def hasNext(self) -> bool:
        return len(self.flattened) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
