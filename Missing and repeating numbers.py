# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:36:35 2023

@author: Shikhar Gupta
"""

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A.sort()
        x=A[0]
        y,z=0,0
        for i in range(1,len(A)):
            if A[i]==x:
                y=x
            elif A[i]-1!=x:
                z=A[i]-1
                x=A[i]
            else:
                x=A[i]
        return [(1,y) if A[0]!=1 else [(x+1,y) if z==0 else (z,y)]]
    
s=Solution()
print(s.repeatedNumber([5, 4,2, 4, 1 ]))