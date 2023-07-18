# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:30:53 2023

@author: Shikhar Gupta
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1,v2=0,0
        while l1:
            v1=(l1.val+v1*10)
            l1=l1.next
        while l2:
            v2=(v2*10+l2.val)
            l2=l2.next
        v=v1+v2
        l3=ListNode(v%10)
        while v//10!=0:
            v=v//10
            temp=ListNode(v%10)
            temp.next=l3
            l3=temp
        return l3