# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:28:56 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,l=0,list(s)
        while True:
            if i==len(l)-1 or i==len(l):
                break
            elif l[i]=='A' and l[i+1]=='B' or l[i]=='C' and l[i+1]=='D':
                l.pop(i)
                l.pop(i)
                i=0
            else:
                i+=1
        return len(l)