# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:36:55 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        l=len(intervals)
        start,end=intervals[0][0],intervals[0][1]
        for i in range(1,l):
            if end>=intervals[i][0]:
                if end<intervals[i][1]:
                    end=intervals[i][1]
            else:
                intervals.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        intervals.append([start,end])
        return intervals[l:]
        
s=Solution()
print(s.merge([[1,4]]))
