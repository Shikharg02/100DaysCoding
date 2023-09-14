# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:07:47 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        i=0
        j=i+2
        while j<4:
            if s1[i]==s2[i] and s1[j]==s2[j]:
                i+=1
                j+=1
            elif s1[i]==s2[j] and s1[j]==s2[i]:
                i+=1
                j+=1
            else:
                return False
        else:
            return True
                