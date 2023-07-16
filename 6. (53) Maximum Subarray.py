# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:28:56 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum,s=0,-10001
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum>s:
                s=sum
            if sum<0:
                sum=0
        return s
