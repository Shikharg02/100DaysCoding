# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:28:56 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        [l.append([0]*(i+1)) for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if (j==0 and i==0) or j==0 or j==i:
                    l[i][j]=1
                else:
                    l[i][j]=l[i-1][j-1]+l[i-1][j]
        return l
