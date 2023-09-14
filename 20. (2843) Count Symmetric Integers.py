# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:09:08 2023

@author: Shikhar Gupta
"""

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        for i in range(low, high+1):
            l=len(str(i))
            s=e=0
            if l%2==0:
                for j in range(l/2):
                    s+=int(str(i)[j])
                    e+=int(str(i)[-j-1])
                if s==e:
                    count+=1
        return count