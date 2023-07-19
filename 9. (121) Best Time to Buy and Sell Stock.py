# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:28:56 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p,stock=0,prices[0]
        for i in prices[1::]:
            if stock>i:
                stock=i
            else:
                x=i-stock
                max_p=max(max_p,x)
        return max_p