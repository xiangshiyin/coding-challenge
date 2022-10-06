#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque

        q = deque([0])
        visited = set([0])
        while q:
            r = q.popleft()
            for k in rooms[r]:
                if k not in visited:
                    q.append(k)
                    visited.add(k)
        return len(visited) == len(rooms)


# @lc code=end
