# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:28:56 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=len(s)/2
        lst=list(s)
        for i in range(x):
            if s[i]==s[-i-1]:
                continue
            else:
                if s[i]>s[-i-1]:
                    lst[i]=s[-i-1]
                else:
                    lst[-i-1]=s[i]
        return ''.join(lst)