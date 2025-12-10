class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # exceptions
        if intervals == None:
            return None
        N = len(intervals)

        if N == 1:
            return [intervals[0]]
        # sort the list
        intervals2 = sorted(intervals, key=lambda x: x[0])
        print(intervals2)
        # merge the intervals
        output = [intervals2[0]]
        for i in range(1, N):
            if intervals2[i][0] <= output[-1][1] and intervals2[i][1] > output[-1][1]:
                output[-1][1] = intervals2[i][1]
            elif intervals2[i][0] > output[-1][1]:
                output.append(intervals2[i])
            print(output)
        return output
