# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:28:56 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,c1,c2=0,0,0
        l=len(nums)
        while i<l:
            x=nums.pop(0)
            if x==0:
                nums.append(0)
            elif x==1:
                nums.insert(l-i-1+c2+c1,1)
                c1+=1
            elif x==2:
                nums.insert(l-i-1+c2,2)
                c2+=1
            i+=1
        nums[::]=nums[::-1]
        return nums