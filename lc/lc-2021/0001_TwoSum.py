# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:00:11 2017

@author: xyin
"""

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rlist = []
        checked = []
        tb_lookup = self.createDict(nums)
        # print(tb_lookup)
        for index, num in enumerate(nums):
            matches = tb_lookup.get(target - num, None)
            # print(num, matches)
            if matches is not None:
                for match in matches:
                    # print(match, index)
                    if match != index and match not in checked:
                        checked.extend([index, match])
                        rlist.append([index, match])
        if len(rlist) == 1:
            rlist = rlist[0]
        return rlist

    def createDict(self, nums):
        tb_lookup = {}
        for index, num in enumerate(nums):
            if tb_lookup.get(num, None) is not None:
                tb_lookup[num].append(index)
            else:
                tb_lookup[num] = [index]
        return tb_lookup


## on 12/24/2020
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # exceptions
        if nums is None or target is None:
            return None
        N = len(nums)
        if N <= 1:
            return []

        # traverse the list
        tb = {}
        for idx, num in enumerate(nums):
            if target - num in tb:
                return [tb[target - num], idx]
            if num not in tb:
                tb[num] = idx
        return []
