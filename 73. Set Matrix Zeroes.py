# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:30:53 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        d=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    d.append((i,j))
        for a in d:
            for i in range(len(matrix)):
                matrix[i][a[1]]=0
            for j in range(len(matrix[0])):
                matrix[a[0]][j]=0
        return matrix