# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:57:47 2023

@author: Shikhar Gupta
"""
########### Not recomended for interviews due to global assignment
'''
count=0                 # global assignment of count
def merge(a, s, m, e):
    left=s
    right=m+1
    temp=[]
    while left<=m and right<=e:
        if a[left]<=a[right]:
            temp.append(a[left])
            left+=1
        else:
            temp.append(a[right])
            global count
            count+=m-left+1             #counted and added each time
            right+=1
    while right<=e:
        temp.append(a[right])
        right+=1
    while left<=m:
        temp.append(a[left])
        left+=1
    print(s,e,temp)
    for i in range(s,e+1):
        a[i]=temp[i-s]

def mergesort(a,start,end):
    if start==end:
        return 
    mid=(end+start)//2
    mergesort(a, start, mid)
    mergesort(a, mid+1, end)
    a=merge(a, start, mid, end)
'''
# Coded using merge sort 
def merge1(a, s, m, e):
    left=s
    right=m+1
    cnt=0                               #local
    temp=[]
    while left<=m and right<=e:
        if a[left]<=a[right]:
            temp.append(a[left])
            left+=1
        else:
            temp.append(a[right])
            global count
            cnt+=m-left+1             #counted and added
            right+=1
    while right<=e:
        temp.append(a[right])
        right+=1
    while left<=m:
        temp.append(a[left])
        left+=1
    for i in range(s,e+1):
        a[i]=temp[i-s]
    return cnt

def mergesort(a,start,end):
    cnt=0
    if start==end:
        return cnt 
    mid=(end+start)//2
    cnt+=mergesort(a, start, mid)           #added cnt in each mergesort
    cnt+=mergesort(a, mid+1, end)           #added cnt in each mergesort
    cnt+=merge1(a, start, mid, end)         #added cnt in each merging
    return cnt
