# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         '''
#         This solution didn't consider the limit of 2 people per boat
#         '''
#         N = len(people)
#         # exceptions
#         if N==1:
#             return N

#         # sort the list O(nlogn)
#         people.sort()

#         # traverse the list
#         l = 0
#         r = N-1
#         boat = [0]
#         while l<r:
#             if boat[-1]+people[l]+people[r]<=limit:
#                 boat[-1] += people[l]+people[r]
#                 l += 1
#                 r -= 1
#             else:
#                 if boat[-1]+people[r]<=limit:
#                     boat[-1] += people[r]
#                     r -= 1
#                 elif boat[-1]+people[l]<=limit:
#                     boat[-1] += people[l]
#                     l += 1
#                 else:
#                     boat.append(people[r])
#                     r -= 1
#         # when l meets r
#         if l==r:
#             if boat[-1]+people[l] <= limit:
#                 boat[-1] += people[l]
#             else:
#                 boat.append(people[l])

#         # return the number of boats
#         return len(boat)

# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         '''
#         This solution considers the limit of 2 people per boat
#         '''
#         N = len(people)
#         # exceptions
#         if N==1:
#             return N

#         # sort the list O(nlogn)
#         people.sort()

#         # traverse the list
#         l = 0
#         r = N-1
#         boat = [0]
#         counter = 0
#         while l<r:
#             if counter<2:
#                 if boat[-1]+people[r]<=limit:
#                     boat[-1] += people[r]
#                     counter += 1
#                     r -= 1
#                 elif boat[-1]+people[l]<=limit:
#                     boat[-1] += people[l]
#                     counter += 1
#                     l += 1
#                 else:
#                     boat.append(people[r])
#                     counter = 1
#                     r -= 1
#             else:
#                 boat.append(people[r])
#                 counter = 1
#                 r -= 1

#         print(boat, l, r)
#         # when l meets r
#         if l==r:
#             if counter<2 and boat[-1]+people[l] <= limit:
#                 boat[-1] += people[l]
#             else:
#                 boat.append(people[l])

#         # return the number of boats
#         return len(boat)


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        This solution considers the limit of 2 people per boat
        """
        N = len(people)
        # exceptions
        if N == 1:
            return N

        # sort the list
        people.sort()

        # traverse the list
        l = 0
        r = N - 1
        num = 0

        while l <= r:
            num += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
        return num
