# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:06:01 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        c=0
        if len(words)!=len(s):
            return False
        for i in words:
            if i[0]!=s[c]:
                return False
            c+=1
        return True