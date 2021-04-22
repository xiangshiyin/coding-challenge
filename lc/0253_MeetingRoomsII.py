class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the intervals
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        # create a heap to record minimum right bound
        from heapq import heappush, heappop
        hp = []
        heappush(hp, intervals[0][1])
        
        # iterate through the list, update the counter
        counter = 1
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1] and (counter == 1 or intervals[i][0] < hp[0]):
                counter += 1
                heappush(hp, intervals[i][1])
            else:
                heappop(hp)
                heappush(hp, intervals[i][1])
        return counter
        