# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:25:23 2018

@author: guyo
"""

def Search(a,n,searchValue):
    for i in range(n):
        if a[i] == searchValue:
            return i
    return -1

def Search_sorted(a,n,searchValue):
    for i in range(n):
        if a[i] >= searchValue:
            break
    if a[i] == searchValue:
        return i
    else:
        return -1