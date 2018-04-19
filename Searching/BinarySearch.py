# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:31:27 2018

@author: guyo
"""

def BinarySearch(a, n , searchValue):
    first = 0 
    last = n-1
    while first <=last:
        mid =(first+last)//2
        if searchValue < a[mid]:
            last = mid-1
        elif searchValue > a[mid]:
            first = mid+1
        else:
            return mid
    return -1
def BinarySearch_rec(a, n, searchValue):
    return _search(a, 0, n-1, searchValue)
def _search(a,first, last, searchValue):
    if first > last:
        return -1
    mid = (first+last)//2
    if a[mid] > searchValue:
        return _search(a,first,mid-1,searchValue)
    elif a[mid] == searchValue:
        return _search(a,mid+1, last, searchValue)
    else:
        return mid
    