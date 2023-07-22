# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:36:35 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lis = [0] * n
        fq = [0] * n
        lis[0] = 1
        fq[0] = 1
        lo = 1

        for i in range(1, len(nums)):
            mx = 0
            c = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if lis[j] > mx:
                        mx = lis[j]
                        c = fq[j]
                    elif lis[j] == mx:
                        c += fq[j]
            fq[i] = c
            lis[i] = mx + 1
            if lo < lis[i]:
                lo = lis[i]

        return lis.count(lo)
    
s=Solution()
nums = [2,2,2,2,2]
print(s.findNumberOfLIS(nums))