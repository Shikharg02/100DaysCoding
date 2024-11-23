# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:36:55 2023

@author: Shikhar Gupta
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        for i in range(r):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(r):
            matrix[i].reverse()
        return matrix