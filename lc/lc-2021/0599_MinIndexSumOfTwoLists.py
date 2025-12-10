# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         # build lookup table
#         tb1 = {v:i for i,v in enumerate(list1)}
#         tb2 = {v:i for i,v in enumerate(list2)}

#         # traverse list1
#         leastSum = len(list1) + len(list2) - 2
#         output = []

#         for v in list1:
#             if v in tb2: # common
#                 if tb1[v] + tb2[v] < leastSum:
#                     output = [v]
#                     leastSum = tb1[v] + tb2[v]
#                 elif tb1[v] + tb2[v] == leastSum:
#                     output.append(v)
#         return output


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # build lookup table
        tb1 = {v: i for i, v in enumerate(list1)}

        # traverse list2
        leastSum = len(list1) + len(list2) - 2
        output = []

        for i, v in enumerate(list2):
            if v in tb1:  # common
                if tb1[v] + i < leastSum:
                    output = [v]
                    leastSum = tb1[v] + i
                elif tb1[v] + i == leastSum:
                    output.append(v)
        return output
